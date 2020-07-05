clear
green='\e[1;32m'
cyan='\e[1;36m'
red='\e[1;31m'
blue='\e[1;34m'
white='\e[1;35m'
yellow='\e[1;33m'
echo -e $red " ";
echo -e $red "________  ________  ___  ________ ________   ";
echo -e $red "|\   ____\|\   __  \|\  \|\  _____\\  _____\ ";
echo -e $red "\ \  \___|\ \  \|\  \ \  \ \  \__/\ \  \__/  ";
echo -e $red " \ \  \  __\ \   _  _\ \  \ \   __\\ \   __\ ";
echo -e $red "  \ \  \|\  \ \  \\  \\ \  \ \  \_| \ \  \_| ";
echo -e $red "   \ \_______\ \__\\ _\\ \__\ \__\   \ \__\  ";
echo -e $red "    \|_______|\|__|\|__|\|__|\|__|    \|__|  ";
echo -e $red "                                             ";
echo -e $green " Script By:$red WHOAMI?"
echo
echo
echo -e $red"[$blue 1$red ]$green My Ip"
echo
echo -e $red"[$blue 2$red ]$green Info Ip and Site"
echo
echo -e $red"[$blue 3$red ]$green Host DNS Finder"
echo
echo -e $red"[$blue 4$red ]$green Scanner Port"
echo
echo -e $red"[$blue 5$red ]$green Host Finder"
echo
echo -e $red"[$blue 6$red ]$green Info Domain"
echo
echo -e $red"[$blue 7$red ]$green Extract Links"
echo
echo -e $red"[$blue 0$red ]$green EXIT"
echo
echo
read -p "Enter The Number : " ipp
if [ $ipp = 1 ]
then
echo -e $cyan
ip=$(curl -s https://api.ipify.org)
echo "My Public IP address Is : $ip"
echo
echo -e $blue
read -p "Press Any Key To Continue" enter
bash Griff.sh
fi
if [ $ipp = 2 ]
then
echo
read -p "Enter The Ip Or Site : " ip
curl http://ip-api.com/$ip
echo
echo -e $blue
read -p "Press Any Key To Continue" enter
bash Griff.sh
fi
if [ $ipp = 3 ]
then
echo
read -p "Enter The Site : " site
curl https://api.hackertarget.com/mtr/?q=$site
echo
echo -e $blue
read -p "Press Any Key To Continue" enter
bash Griff.sh
fi
if [ $ipp = 4 ]
then
echo
read -p "Enter The Ip Or Site : " port
curl http://api.hackertarget.com/nmap/?q=$port
echo
echo -e $blue
read -p "Press Any Key To Continue" enter
bash Griff.sh
fi

if [ $ipp = 5 ]
then
echo
read -p "Enter The Site : " s
s=$(curl -s http://api.hackertarget.com/hostsearch/?q=$s)
echo "The Host Is : $s"
echo
echo -e $blue
read -p "Press Any Key To Continue" enter
bash Griff.sh
fi
if [ $ipp = 6 ]
then
echo
read -p 'Enter The Domain : ' mail
curl -H "Accept: application/json" \
https://check-host.net/check-tcp?host=smtp://$mail&max_nodes=1
echo
echo -e $blue
echo
echo
read -p "Press Any Key To Continue" enter
bash Griff.sh
fi
if [ $ipp = 7 ]
then
echo
read -p "Enter The Domain : " df
echo -e $red
curl https://api.hackertarget.com/pagelinks/?q=$df
echo
echo -e $blue
read -p "Press Any Key To Continue" enter
bash Griff.sh
fi
if [ $ipp = 0 ]
then
clear
echo
echo
echo
echo
echo
echo -e $green "WHATSAPP :$red 53052819**"
echo
echo
echo
echo
exit
else
bash Griff.sh
fi
