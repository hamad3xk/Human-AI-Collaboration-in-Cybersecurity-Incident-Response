from scipy import stats

def shapiro_p(x): return stats.shapiro(x).pvalue
def levene_p(x, y): return stats.levene(x, y).pvalue
