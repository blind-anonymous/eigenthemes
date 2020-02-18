echo "Metric,Mean,Std-Dev"
awk 'NR>1 {{for(i=1;i<=NF;i++) {sum[i] += $i; sumsq[i] += ($i)^2}}} 
      END {for (i=1;i<=NF;i++) {
      if (i == 1) printf "Precision@1,%f,%f\n", sum[i]/(NR-1), sqrt((sumsq[i]-sum[i]^2/(NR-1))/(NR-2));
      else printf "MRR,%f,%f\n", sum[i]/(NR-1), sqrt((sumsq[i]-sum[i]^2/(NR-1))/(NR-2));
      }}' $1

#awk 'NR>1 {{for(i=1;i<=NF;i++) {printf "%i %f \n", i, $i}}}' results/aida_testb_le_titov.tsv
