
bla = read.csv("group_size_dt.csv", head = F) 

lambda = 1/mean(bla$V1)
kkk = hist(bla$V1,breaks=seq(0,max(bla$V1)+1,by=1))

print(1/lambda)

bla2 = rexp(200000,lambda)
kkk2 = hist(bla2,breaks = seq(0,max(bla2)+1,by=1))

a = kkk$density
b = kkk2$density

png("group_size1.png")
plot(kkk$mids,a,main="PDF",xlab="Group Size")
lines(kkk2$mids,b,col="red",lwd=3)
dev.off()

a = cumsum(kkk$density)
b = cumsum(kkk2$density)

png("group_size3.png")
plot(kkk$mids,a,main="CDF",xlab="Group Size")
lines(kkk2$mids,b,col="red",lwd=3)
dev.off()

a = 1-cumsum(kkk$density)
b = 1-cumsum(kkk2$density)

png("group_size2.png")
plot(kkk$mids,a, main="ECCDF Dartmouth",log="xy",xlab="Group Size")
lines(kkk2$mids,b,col="red",lwd=3)
dev.off()


