import requests

def get_transaction_info(tx_hash):
    url = f"https://blockchain.info/rawtx/{tx_hash}"
    response = requests.get(url)
    if response.status_code == 200:
        transaction_info = response.json()
        return transaction_info
    else:
        print("Ошибка при запросе транзакции:", response.status_code)
        return None

# Пример использования
tx_hash = "ваш_хэш_транзакции"
transaction_info = get_transaction_info(tx_hash)
if transaction_info:
    print("Информация о транзакции:")
    print(transaction_info)
