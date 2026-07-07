import socket 
from scapy.all import sniff, IP, TCP, UDP

Remote_Server_IP = "192.168.1.100"
Remote_Server_Port = 4646

# Manuel soket oluşturuyoruz bu işlem os çekirdeğinde doğrudan bir udp portu açar
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def cikar_ve_gonder(paket):
    #Yakalanan her paketin metrikleri çıkarılır ve UDP üzerinden uzak sunucuya göndeirilir
    if IP in paket:
        src_ip = paket[IP].src
        dst_ip = paket[IP].dst
        protocol = paket[IP].proto
        payload_size = len(paket)

        # Metrikleri log formatında hazırlama
        metrik_veri= f"SRC:{src_ip} | DST:{dst_ip} | Protocol:{protocol} | LEN:{payload_size} bytes"

        # string veriyi byte dizisine çevirerek UDP soketinden yollama
        udp_socket.sendto(metrik_veri.encode('utf-8'), (Remote_Server_IP, Remote_Server_Port))
        print(f"[+] Gönderilen veriler: {metrik_veri}")

def snifferi_baslat():
    print("[*] Paket yakalama başlatalidi...")
    # filter = ip: sadece ip katmanına sahip paketleri yakalar arp felan onlar elenir
    # store = False: bellek adreslemesini şişirmemek için paketleri RAM'de tutmaz
    sniff(filter="ip",prn=cikar_ve_gonder, store=False)

if __name__ == "__main__":
    try:
        snifferi_baslat()
    except KeyboardInterrupt:
        print("\n[!] Sniffer durduruldu.")
    finally:
        udp_socket.close()