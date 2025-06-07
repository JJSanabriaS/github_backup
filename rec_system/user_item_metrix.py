
import seaborn as sns
_= np.nan
scores =np.array([[5,4,4,1],
                  [2,3,3,4.5],
                  [3,2,3,4],
                  [4,4,5,_],
                  [3,_,_,_]])
sns.heatmap(scores,annot=True,fmt=".1f",
xticklabels=['Gouda','Chevre','Emmentaler','Brie',],
yticklabels=['A','B','C','D','E',]
)
