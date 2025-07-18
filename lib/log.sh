# lib/log.sh

log_info() {
local message=$1
if [ "$_MYTOOL_VERBOSE" -eq 1 ]; then
	echo "[$(date +"%d-%m-%Y %H:%M:%S")]-[INFO]: $message"
fi
}

log_error() {
local message=$1
local script_name="${BASH_SOURCE[1]##*/}"
local line_NO="${BASH_LINENO[0]}"

echo "[$(date +"%d-%m-%Y %H:%M:%S")]-[ERROR]-[${script_name}:${line_NO}]: $message" >&2
}

show_help() {
echo "Usage: ./mytool.sh <command> [arguments]"
echo""
echo "Commands:"
echo " greet <name>     : Greets specified name."
echo " ping <host>      : Pings the specified host."
echo " deploy <env>     : Deploys to the specified environment (e.g., 'staging', 'production'). "
echo " help             : Displays help message. "
echo ""
}
