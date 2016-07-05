b = read.csv("result_bubble.0.txt",head=F, sep = ",")
#p = read.csv("result_bubble.1.txt",head=F, sep = ",")
#f = read.csv("result_bubble.2.txt",head=F, sep = ",")

total =length(b$V1)

b = b[b$V3!="False",]
ub = length(b$V1)
tb=mean(b$V5)
mb=mean(b$V4)
#png("comp.png")
#par(mfrow=c(1,2))
#boxplot(p$V4,b$V4,names = c("protocolo","bubble"),main="Messages Transmitted")

x = c(1,3,6,12,24,48,96,7*24,14*24,21*24,42*24)

avb1 = mean(b[b$V5<1,]$V5)
avb2 = mean(b[b$V5<3,]$V5)
avb3 = mean(b[b$V5<6,]$V5)
avb4 = mean(b[b$V5<12,]$V5)
avb5 = mean(b[b$V5<24,]$V5)
avb6 = mean(b[b$V5<48,]$V5)
avb7 = mean(b[b$V5<96,]$V5)
avb8 = mean(b[b$V5<7*24,]$V5)
avb9 = mean(b[b$V5<14*24,]$V5)
avb10 = mean(b[b$V5<21*24,]$V5)
avb11 = mean(b[b$V5<42*24,]$V5)


y1= c(avb1,avb2,avb3,avb4,avb5,avb6,avb7,avb8,avb9,avb10,avb11)

png("delay_log.png")
plot(x,y1, type="b",col="blue",ylim = c(0,avb11),ylab="Avg. Delivery time(h)",xlab = "Message TTL",lty=2,lwd=3,pch=0,log="x",main = "Delay w/ 5 Relay Points")
#plot(x,100*y1,log="x",col="blue",type="b",ylim=c(0,70))
legend('topleft', c("Popularity Only","No Relay Points","Radius of Gyration + Popularity") , lty=1, col=c('pink','blue', 'red'), bty='n', cex=.75,lwd = 2,pch=c(8,0,4))
dev.off()

#png("boxplot.png")
#boxplot(p[p$V5<48,]$V5,b[b$V5<48,]$V5,names = c("protocolo","bubble"),main="Delivery times")
#dev.off()

bt1 = length(b[b$V5 <=1,]$V1)/total

bt2 = length(b[b$V5 <=3,]$V1)/total

bt3 = length(b[b$V5 <=6,]$V1)/total


bt4 = length(b[b$V5 <=12,]$V1)/total

bt5 = length(b[b$V5 <=24,]$V1)/total

bt6 = length(b[b$V5 <=48,]$V1)/total

bt7 = length(b[b$V5 <=96,]$V1)/total

bt8 = length(b[b$V5 <=7*24,]$V1)/total

bt9 = length(b[b$V5 <=14*24,]$V1)/total

bt10 = length(b[b$V5 <=21*24,]$V1)/total

bt11 = length(b[b$V5 <=42*24,]$V1)/total

x = c(1,3,6,12,24,48,96,7*24,14*24,21*24,42*24)
y1= c(bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,bt10,bt11)

png("deliv_log.png")
plot(x,100*y1, type="b",col="blue",ylim = c(0,115),ylab="Delivery Ratio (%)",xlab = "Time(h)",lty=2,lwd=3,pch=0,log="x",main = "Delivery Ratio w/ 5 Relay Points")
legend('topleft', c("Popularity Only","No Relay Points","Radius of Gyration + Popularity") , lty=1, col=c('pink','blue', 'red'), bty='n', cex=.75,lwd = 2,pch=c(8,0,4))
dev.off()


bt1 = sum(read.csv("b_1h.txt",head=F))/total

bt2 = sum(read.csv("b_3h.txt",head=F))/total

bt3 = sum(read.csv("b_6h.txt",head=F))/total

bt4 = sum(read.csv("b_12h.txt",head=F))/total

bt5 = sum(read.csv("b_24h.txt",head=F))/total

bt6 = sum(read.csv("b_48h.txt",head=F))/total

bt7 = sum(read.csv("b_96h.txt",head=F))/total

bt8 = sum(read.csv("b_1w.txt",head=F))/total

bt9 = sum(read.csv("b_2w.txt",head=F))/total

bt10 = sum(read.csv("b_3w.txt",head=F))/total

bt11 = sum(read.csv("b_6w.txt",head=F))/total

x = c(1,3,6,12,24,48,96,7*24,14*24,21*24,42*24)
y1= c(bt1,bt2,bt3,bt4,bt5,bt6,bt7,bt8,bt9,bt10,bt11)

png("overhead_log.png")
plot(x,y1, type="b",col="blue",ylim = c(0,bt11+10),ylab="# of Transmissions/Message",xlab = "Time(h)",lty=2,lwd=3,pch=0,log="x",main = "Network Overhead w/ 5 Relay Points")
#plot(x,100*y1,log="x",col="blue",type="b",ylim=c(0,70))
legend('topleft', c("Popularity Only","No Relay Points","Radius of Gyration + Popularity") , lty=1, col=c('pink','blue', 'red'), bty='n', cex=.75,lwd = 2,pch=c(8,0,4))
dev.off()


