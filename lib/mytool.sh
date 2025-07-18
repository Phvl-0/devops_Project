#!/bin/bash

#----Robust script Header----#
set -euo pipefail
#set -x

#-------Comprehensive logging-------#
exec > >(tee -a mytool.log) 2>&1

_MYTOOL_VERBOSE=0

#----Sourcing functions----#
source "./lib/log.sh"
source "./lib/commands.sh"
source "./lib/validate.sh"

#-------------------------------#
cleanup() {
#sleep 1
#ScriptName="$0"
#log_info "[+] '${ScriptName##*/}' Script Ended!"
:
}
trap cleanup EXIT
#-------------------------------#

while [[ "$#" -gt 0 ]]; do
	case "$1" in
		-v|--verbose)
			_MYTOOL_VERBOSE=1
			log_info "[!] Verbose mode enabled (via $1)."
			shift
			;;
		--)
			shift
			break
			;;
		-*)
			log_error "[-] Unknown global flag: '$1'"
			show_help
			exit 1
			;;
		*)
			break
			;;
	esac
done



#------------Main script--------#

#check if ay argumets are provided
if [ "$#" -eq 0 ]; then
	log_error "[-] NO command provided!"
	show_help
	exit 1
fi

#------------------------------------------------#


COMMAND="$1"
shift
case "$COMMAND" in
	"greet")
		cmd_greet "$@"
		;;
	"ping")
		cmd_ping "$@"
		;;
	"deploy")
		cmd_deploy "$@"
		;;

	"help")
		show_help 
		;;
	*)
		log_error "[-] Unknown command: '$COMMAND'"
		show_help
		exit 1
		;;
esac


