import matplotlib.pyplot as plt

def genereta_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def genereate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [10, 20, 30]
    #genereta_bar_chart(labels, values)
    genereate_pie_chart(labels, values)