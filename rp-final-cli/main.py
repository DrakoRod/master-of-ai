import click

from decision_tree import train_decision_tree


@click.group()
def main():
    pass

@main.command()
def decision_tree():
    print('Arbol de Decision')
    train_decision_tree()

@main.command()
def kmeans():
    print('K Means')

@main.command()
def regressions():
    print('Regressión')

@main.command()
@click.option('--measure', '-m', is_flag=True, default=True)
def perceptron():
    print('Regressión')


if __name__ == "__main__":
    main()