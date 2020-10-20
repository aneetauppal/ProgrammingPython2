

PDB.data<-read.table("/Users/aneetauppal/Downloads/VEB1_dihedrals.txt", header=FALSE, comment.char="", row.names=1,
                       colClasses=c("character", "numeric", "numeric"), 
                       col.names=c("name", "phi", "psi"))

scatter.phi <- PDB.data[,c("phi")]
scatter.psi <- PDB.data[,c("psi")]

par(pty="s")
#plot(scatter.phi, scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="VEB1", pch=20, xlab=expression(psi), ylab=expression(phi), cex=.3, asp=1.0)

z = rep(1,275)
library(gplots)

i=0
J=0
Density_data = matrix(0,nrow = 15, ncol=15)
for(phii in seq(-180,154,by=24))
{
  i=i+1
  j=0
  for(psii in seq(-180,156,by=24))
  {
    j=j+1
    Density_data[i,j] = length(subset(scatter.phi,((scatter.phi > phii)&(scatter.phi < phii+24))&((scatter.psi > psii)&(scatter.psi < psii+24))))
  }
}


#length(subset(scatter.psi,((x > -180)&(x < -170))&((y > -180)&(y < -170))))
#Density_data

filled.contour(x=seq(-180,180,length.out = nrow(Density_data)),y=seq(-180,180,length.out = nrow(Density_data)),Density_data, main="VEB1", xlab = (xlab=expression(psi)), ylab = (ylab=expression(phi)),col=colorpanel(15, "white", "blue"), nlevels=50,
               plot.axes = { axis(1); axis(2); points(scatter.phi, scatter.psi, cex=.4,) })


x.test = (PDB.data[,c("phi")] +180)/360
y.test = (PDB.data[,c("psi")] +180)/360
par(mfrow=c(1, 1))

