#set terminal pdf
#set title "{/*1.4 Tangente Hiperbólica}"
#set output "tanh.pdf"
#plot tanh(x)

#set terminal pdf
#set title "{/*1.4 Linear}"
#set output "linear.pdf"
#set xrange[-1:1]
#set grid
#plot x

#set terminal pdf
#set title "{/*1.4 Sigmóide}"
#set output "sigmoide.pdf"
#plot 1/(1+exp(-x)) title 'sigmoide'

#set terminal pdf
#set title "{/*1.4 Step}"
#set output "step.pdf"
#set grid
#set yrange[0:1]
#set xrange[-1:1]
#f(x) = (x<0)?0:1
#plot f(x) lw 2

#set terminal pdf
#set title "{/*1.4 ReLu}"
#set output "relu.pdf"
#set grid
#set yrange[0:1]
#set xrange[-1:1]
#f(x) = (x<0)?0:x
#plot f(x) lw 2 title 'ReLu'

set terminal pdf
set title "{/*1.4 SoftPlus}"
set output "softplus.pdf"
set grid
f(x) = log(1+exp(x))
plot f(x) lw 2 title 'SoftPlus'