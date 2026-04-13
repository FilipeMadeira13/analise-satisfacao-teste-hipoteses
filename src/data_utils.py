import numpy as np
import pandas as pd


def gerar_dados_satisfacao(seed: int = 42, n: int = 100) -> pd.DataFrame:
    """Gera um dataset sintético de satisfação antes/depois para análise."""
    np.random.seed(seed)

    antes = np.random.normal(loc=7.0, scale=1.5, size=n)
    depois = np.random.normal(loc=7.5, scale=1.5, size=n)

    df = pd.DataFrame(
        {
            "satisfacao_antes": antes,
            "satisfacao_depois": depois,
        }
    )

    return df.clip(lower=0, upper=10)


def salvar_dados_csv(df: pd.DataFrame, path: str) -> None:
    """Salva o dataset em um arquivo CSV."""
    df.to_csv(path, index=False)


if __name__ == "__main__":
    import os

    df = gerar_dados_satisfacao()
    os.makedirs("data", exist_ok=True)
    salvar_dados_csv(df, "data/satisfacao_simulada.csv")
    print("Dados gerados em data/satisfacao_simulada.csv")
