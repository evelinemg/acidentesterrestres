import os
from google.cloud import storage
storage_client = storage.Client()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="caminho_chave.json"
def cria_bucket(bucket_nome):
    """
    Cria bucket com localização pré-definida
    """
    # bucket_nome = "nome-da-nova-bucket"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_nome)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Bucket {} criada em {} com classe {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket


def lista_buckets():
    """Lista de buckets"""

    buckets = storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

def upload_objeto(bucket_name, source_file_name, destination_blob_name):
    """Upload de aquivos na bucket"""
    # O ID da GCS bucket
    # bucket_name = "nome-da-bucket"
    # O caminho do arquivo a ser enviado
    # source_file_name = "local/caminho/para/arquivo"
    # O ID do objeto na bucket
    # destination_blob_name = "nome-objeto-bucket"

    
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name, timeout=(500000,5000000.0))

    print(
        "Arquivo {} enviado para {}.".format(
            source_file_name, destination_blob_name
        )
    )


def lista_objetos(bucket_name):
    """Lista todos os objetos da pasta"""
    # bucket_nome = "nome-objetos-bucket"
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)
        
def novapasta(bucket_name, destination_folder_name):
    """Cria nova pasta vazia na bucket"""
    bucket = storage_client.get_bucket(bucket_name, timeout=50000.0)
    blob = bucket.blob(destination_folder_name)
    #blob.upload_from_string('')
    print("Pasta {} criada".format(destination_folder_name))
