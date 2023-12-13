import subprocess
import platform
import sentry_sdk

sentry_sdk.init(
    dsn="https://bfdcf1d1483c6b8d6ecbbf4b4e65cbf9@o4506125225099264.ingest.sentry.io/4506163784974336",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)

PACOTES_WINDOWS = {
    0: "Todas as aplicações",
    1: "JetBrains.PyCharm.Community.EAP",
    2: "Python.Python.3.11",
    3: "Oracle.MySQL",
    4: "Microsoft.VisualStudioCode",
    5: "PostgreSQL.pgAdmin",
    6: "Oracle.JDK.21",
    7: "JetBrains.IntelliJIDEA.Community",
    8: "OpenJS.NodeJS",
    9: "MongoDB.Server",
    10: "MongoDB.Compass.Full",
    11: "Apache.CouchDB",
    12: "Git.Git",
    13: "PuTTY.PuTTY",
    14: "SWI-Prolog.SWI-Prolog",
    15: "logisim-evolution.logisim-evolution",
    16: "Orwell.Dev-C++",
    17: "Redisant.RedisAssistant",
    18: "Google.FirebaseCLI",
    19: "GeoGebra.GraphingCalculator"
}

# Pacotes Linux
PACOTES_LINUX = {
    0: "Todas as aplicações",
    1: "JetBrains.PyCharm.Community.EAP",
    2: "Python.Python.3.11",
    3: "JGraph.Draw",
    4: "Oracle.MySQL",
    5: "Microsoft.VisualStudioCode",
    6: "PostgreSQL.pgAdmin",
    7: "Oracle.JDK.21",
    8: "JetBrains.IntelliJIDEA.Community",
    9: "OpenJS.NodeJS",
    10: "MongoDB.Server",
    11: "MongoDB.Compass.Full",
    12: "Redis",
    13: "Apache.CouchDB",
    14: "Git.Git",
    15: "PuTTY.PuTTY",
    16: "cSWI-Prolog.SWI-Prolog",
    17: "Canonical.Ubuntu.2204",
    18: "Docker.DockerDesktop",
    19: "logisim-evolution.logisim-evolution",
    20: "Orwell.Dev-C++",
    21: "Redisant.RedisAssistant",
    22: "Google.FirebaseCLI 12.9.1",
    23: "GeoGebra.GraphingCalculator",
}


def install_package(package_name):
    if platform.system() == "Windows":
        command = f"winget install {package_name} --silent"
    else:
        command = f"sudo apt install {package_name} --yes"
    subprocess.run(command, shell=True)


def install_all_packages(packages):
    for package_name in packages.values():
        install_package(package_name)


def main():
    print("Escolha uma opcao para instalacao:")

    packages = PACOTES_WINDOWS if platform.system() == "Windows" else PACOTES_LINUX

    for key, value in packages.items():
        print(f"{key}. Instalar {value}")

    try:
        opcoes = input("Digite os numeros das opcoes desejadas separados por espaco (ou 0 para instalar todos): ")
        opcoes = list(map(int, opcoes.split()))

        if 0 in opcoes:
            install_all_packages(packages)
        else:
            for opcao in opcoes:
                if opcao in packages:
                    install_package(packages[opcao])
                else:
                    print(f"Opcao {opcao} invalida!")

    except ValueError:
        print("Por favor, insira numeros separados por espaco.")
    except Exception as e:
        sentry_sdk.capture_exception(e)
        print("Ocorreu um erro durante a execucao do programa.")


if __name__ == "__main__":
    main()

    input("Pressione Enter para fechar...")
