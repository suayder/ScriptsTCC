import glob
import matplotlib.pyplot as plt
import numpy as np
import itertools


def plot_confusion_matrix(p,cm, classes,
                          normalize=False,
                          title='Matriz de Confusão',
                          cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')


    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'f'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Classe')
    plt.xlabel('Classe predita pela Wisard')
    plt.savefig('plots/'+str(p)+'_8_confusionMatrix.png')
    plt.show()

def lineChart(x, y, title = 'Gráfico quantidade de entradas por RAM versus media de buracos classificados errôneamente'):

    plt.title(title)
    plt.plot(x,y,marker='o')
    plt.ylabel('Media de classificações erradas')
    plt.xlabel('Quantidade de entrada por RAM')
    #plt.savefig('plots/8_line.png')
    plt.show()

def barChart(x,y, title = 'Gráfico quantidade de entradas por RAM versus media de buracos classificados corretamente'):
    plt.title(title)
    plt.bar(x,y)
    plt.ylabel('Media de classificações corretas')
    plt.xlabel('Quantidade de entrada por RAM')
    #plt.savefig('plots/8_bar.png')
    plt.show()

def confusionMatrixForAll(x,tp, tn, fp, fn, title = 'Análise de resposta dada pela Wisard'):
    plt.plot( x, tp, marker='o', color='skyblue', markersize=6, linewidth=1,label="Verdadeiro positivo")
    plt.plot( x, tn, marker='o', color='olive', markersize=6, linewidth=1, label="Verdadeiro negativo")
    plt.plot( x, fp, marker='o', color="#333333", markersize=6, linewidth=1,label="Falso positivo")
    plt.plot( x, fn, marker='o', color="chocolate", markersize=6, linewidth=1, label="Falso negativo")
    plt.title(title)
    plt.legend()
    plt.ylabel('Respostas da Wisard')
    plt.xlabel('Numero de entrada por RAM')
    plt.savefig('plots/8_answer.png')
    plt.show()


hit = {}
failure = {}

m = np.empty([2,2])
precisions = []
for i in range(10,25):
    paths = glob.glob('07results/'+str(i)+"*.JPG.dat")
    hit[i] = 0
    failure[i] = 0

    print(len(paths))
    for it in paths:
        files = open(it, "r")
        #res = files.read().split('\n')
        #res = res[0]
        res = files.read().split(' ')
        hit[i] = hit[i]+int(res[0])
        failure[i] = failure[i]+int(res[1])

    hit[i] = hit[i]/len(paths)
    failure[i] = failure[i]/len(paths)

#    p = (tp[i]/(tp[i]+fp[i]))
#    r = (tp[i]/(tp[i]+fn[i]))
#    precisions.append(2*(p*r/(p+r)))

    print("precision: ", (hit[i]/(hit[i]+failure[i])))
    #plot_confusion_matrix(i,m, ('Buraco','Não buraco'), False, "Matriz de confusão para o threshold de 0.8")
#confusionMatrixForAll(list(range(10,25)),tp.values(),tn.values(),fp.values(),fn.values())
#barChart(list(range(10,25)),hit.values())
#lineChart(list(range(10,25)), failure.values())