library(ggplot2)
# print 'sample,ntpos,majmin,nt,freq,status'
segarr <- c('PB2','PB1','PA','HA','NP','NA','MP','NS')
# segarr <- c('HA','NA')
# segarr<-c('PB2')
# SEGMENT<-'MP'
# filename <- paste(SEGMENT,'_input.csv',sep='')
for (SEGMENT in segarr){

filename <- paste(SEGMENT,'_coverage_formatted.csv',sep='')

mydata<-read.csv(file=filename,header=T,sep=",")


# mydata<-mydata[which(mydata$majmin=='minor'),]
# FDATA<-mydata[which(mydata$gen==gen),]

p<- ggplot(mydata,aes(x=factor(ntpos),y=coverage,group=sample,color = covertype)) + geom_line() +#geom_line() +# geom_bar(aes(fill = segment,stat='identity'), colour = "black") + #geom_point(aes(size=freq,alpha=0.8)) +
    # theme(axis.ticks = element_blank(), axis.text.x = element_blank()) +
    # theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1,size=8)) +
    # scale_fill_brewer(palette="Set1") + 
    facet_wrap(~ sample, ncol = 4, scales = "free") + 
    scale_color_manual(values=c("#e41a1c", "#4daf4a", "black")) +
    theme(axis.text.x = element_text(size=8)) +
    scale_x_discrete(breaks=seq(0,max(mydata$ntpos),100))# +
    # ylim(0,5000)
    # facet_grid(strain + day ~ gen, scales = "free_y")

ggsave(p, file=paste(SEGMENT,"_coverage_plot.pdf",sep=''), width=15, height=30,limitsize=FALSE)
}



# segarr <- c('PB2','PB1','PA','HA','NP','NA','MP','NS')
# # truefalse <- c('true','FALSE')
# # gen <- c('F0','F1')

# for (seg in segarr){

#     graphme(seg,'F0','true')
#     graphme(seg,'F1','true')
#     graphme(seg,'F0','FALSE')
#     graphme(seg,'F1','FALSE')











# segarr <- c('HA','NA')
# segarr<-c('PB2')
# SEGMENT<-'MP'
# filename <- paste(SEGMENT,'_input.csv',sep='')
# for (SEGMENT in segarr){

# filename <- 'segments_combined.csv'

# mydata<-read.csv(file=filename,header=T,sep=",")


# # mydata<-mydata[which(mydata$majmin=='minor'),]
# # FDATA<-mydata[which(mydata$gen==gen),]

# p<- ggplot(mydata,aes(x=factor(ntpos),y=coverage,group=sample,color = covertype)) + geom_line() +#geom_line() +# geom_bar(aes(fill = segment,stat='identity'), colour = "black") + #geom_point(aes(size=freq,alpha=0.8)) +
#     # theme(axis.ticks = element_blank(), axis.text.x = element_blank()) +
#     # theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust=1,size=8)) +
#     # scale_fill_brewer(palette="Set1") + 
#     facet_grid(segment ~ sample,  scales = "free",space='free') + 
#     scale_color_manual(values=c("#e41a1c", "#4daf4a", "black")) +
#     theme(axis.text.x = element_text(size=8)) +
#     scale_x_discrete(breaks=seq(0,max(mydata$ntpos),100))# +
#     # ylim(0,5000)
#     # facet_grid(strain + day ~ gen, scales = "free_y")

# ggsave(p, file="segments_coverage_plot.pdf", width=100, height=35,limitsize=FALSE)




