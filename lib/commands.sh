# lib/commands.sh

cmd_greet() {
 local _GREET_FORMAL=0 # Default to informal (0 = off, 1 = on)

    # --- Subcommand-Specific Flag Parsing Loop ---
    while [[ "$#" -gt 0 ]]; do
        case "$1" in
            --formal)
                _GREET_FORMAL=1
                log_info "[!] Using formal greeting."
                shift # Consume the --formal argument
                ;;
            -*) # Catch any other unknown flags for this subcommand
                log_error "[-] Unknown flag for 'greet' command: '$1'"
                show_help
                exit 1
                ;;
            *) # Stop processing flags once a non-flag argument (the name) is encountered
                break
                ;;
        esac
    done

    validate_arg "${1:-}" "name" "greet"
    local name="$1"
   
   if [ "$_GREET_FORMAL" -eq 1 ]; then
        echo "[+] Greetings, $name! Welcome to mytool."
    else
        echo "[+] Hello $name! Welcome to mytool."
    fi
}

cmd_ping() {
    # Using the new validation function
    validate_arg "${1:-}" "host" "ping"
    local host="$1"
    echo "[+] Pinging $host..."
    sleep 2
    if  ping -c 4 -q "$host" &> /dev/null; then
        echo "[+] Successfully pinged $host."
    else
	log_error "[-] Failed to ping $host."
	exit 1
    fi
}

cmd_deploy() {
validate_arg "${1:-}" "environment" "deploy"
local environment="$1"
local _DEPLOY_FORCE=0
shift 

while [[ "$#" -gt 0 ]]; do
	case "$1" in
		--force)
			_DEPLOY_FORCE=1
			log_info "[!] Force deployment enabled."
			shift
			;;
		-*)
			log_error "[-] Unknown flag for 'deploy' command: '$1'"
			show_help
			exit 1
			;;
		*)
			log_error "[-] unexpected argument for 'deploy' command: '$1'"
			show_help
			exit 1
			;;
	esac
done
echo "[+] Deploying to $environment environment..."
sleep 3
echo "[*] Please wait..."
sleep 6

if [ "$_DEPLOY_FORCE" -eq 1 ]; then
	echo "[+] Force deployment to $environment completed succesfully!"
else
	echo "[+] Deployment to $environment completed successfully!"
fi

}
