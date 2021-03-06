
bla = read.csv("../duration.csv", head = F) 
kkk = hist(bla$V1,breaks=seq(0,max(bla$V1)+1,by=1))

a = kkk$density
print(min(bla$V1))
a3 = 1-cumsum(kkk$counts/sum(kkk$counts))

bla2 = read.csv("../fit.csv",head=F)
kkk2 = hist(bla2$V1,breaks=seq(min(bla2$V1),max(bla2$V1)+1,by=1))
a4 = 1-cumsum(kkk2$counts/sum(kkk2$counts))

png("pl_fit.png")
plot(kkk$mids,a3, main="ECCDF Dartmouth",log="xy",xlab="Contact Duration",col="red",xlim = c(1,100000),ylim=c(0.0001,1),ylab="P[X>x]")
points(kkk2$mids,a4,lwd=2)
legend("topright", c("empirical","fitting"),col = c("red","black"), pch=c(1,1))
dev.off()
