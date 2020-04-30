version 1.0
task GenerateSBSMatrix{
  input{
    File maf
      Int diskGB
      String? outbase = "results"
  }
  command{
    python /data/dawsonet/sandbox/sigprofilerhelper/generate_matrix.py -m ${maf} \
      -d sigprof_input  && \
      mv sigprof_input/output/SBS/PROJECT.SBS96.all ${outbase}.SBS96.all && \
      tar czf ${outbase}.sigpromatgen.tgz sigprof_input/
  }

  runtime{
  }

  output{
    File countsMatrix = "${outbase}.SBS96.all"
      File resultsTarball = "${outbase}.sigpromatgen.tgz"
  }

}

task GenerateID83Matrix{
  input{
    File maf
      File refFA
      File refFAI
      Int diskGB
      String? outbase = "results"
      String mafBase = basename(basename(maf, ".tsv"), ".maf")
  }

  command{
    python /data/dawsonet/sandbox/presig/presig/presig.py -m ${maf} \
      -f ${refFA} && \
      mv ${mafBase}.ID83.tsv ${outbase}.ID83.tsv
  }

  runtime{
  }

  output{
    File idMatrixTSV = "${outbase}.ID83.tsv"
  }
}

task ExtractSignatures{
  input{
    File countsMatrix
      Int diskGB
      String tag
      Int? threads=16
      Int? memory = ceil(2 * threads)
      Int? startSigs = 1
      Int? endSigs = 8
      Int? iters = 1000
      String? outbase = "extractor"
  }


  command{
    python /data/dawsonet/sandbox/sigprofilerhelper/run_sigprofiler.py -s ${startSigs} \
      -e ${endSigs} \
      -i ${iters} \
      -t ${countsMatrix} \
      -c ${threads} \
      -d ${outbase}.${tag} && \
      tar czf ${outbase}.${tag}.tgz ${outbase}.${tag}
  }

  runtime{
  }

  output{
    File resultsTarball = "${outbase}.${tag}.tgz"
  }
}


task tidySigPlot{
  input{
    File sigTGZ
      String type
      String base = basename(sigTGZ, ".tgz")
  }

  command{
    tar xvzf ${sigTGZ} && \
      Rscript /data/dawsonet/sandbox/tidysig/scripts/make_${type}_plots.R \
      -i ${base} \
      -o ${base}_${type}_plots && \
      tar cvzf ${base}_${type}_plots.tgz ${base}_${type}_plots/
  }
  runtime{
  }
  output{
    File tidysig_plots = "${base}_${type}_plots.tgz"
  }
}

workflow SigprofilerSigs{
  input{
      File maf
      File refFA
      File refFAI
      Int diskGB = ceil((size(maf, "GB") * 2) + 20)
      Int extractThreads
      String tag

      Int? sbs_start = 1
      Int? sbs_end = 7
      Int? sbs_iters = 1000

      Int? id_start = 1
      Int? id_end = 7
      Int? id_iters = 1000
  }


  call GenerateSBSMatrix{
    input:
      maf=maf,
      diskGB=diskGB
  }

  call ExtractSignatures as SBS_Extract{
    input:
      countsMatrix=GenerateSBSMatrix.countsMatrix,
      diskGB=diskGB,
      startSigs = sbs_start,
      endSigs = sbs_end,
      iters = sbs_iters,
      threads=extractThreads,
      outbase="SBS_results",
      tag=tag
  }

  call GenerateID83Matrix{
    input:
      maf=maf,
      refFA=refFA,
      refFAI=refFAI,
      diskGB=diskGB
  }

  call ExtractSignatures as ID83_Extract{
    input:
      countsMatrix=GenerateID83Matrix.idMatrixTSV,
      diskGB=diskGB,
      startSigs = id_start,
      endSigs = id_end,
      iters = id_iters,
      threads=extractThreads,
      outbase="ID83_results",
      tag=tag
  }

  call tidySigPlot as SBSPlot{
    input:
      sigTGZ=SBS_Extract.resultsTarball,
      type="sbs"
  }

  call tidySigPlot as IDPlot{
    input:
      sigTGZ=ID83_Extract.resultsTarball,
      type="id"
  }

  output{
      File tidysig_SBS_plots = SBSPlot.tidysig_plots
      File tidysig_ID_plots = IDPlot.tidysig_plots
      File sbs_results_tarball = SBS_Extract.resultsTarball,
      File id_results_tarball = ID83_Extract.resultsTarball,
      File presig_id_counts = GenerateID83Matrix.idMatrixTSV
  }



}
