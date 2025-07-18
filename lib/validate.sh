# lib/validate.sh

# Checks if a required argument is provided for a subcommand
validate_arg() {
    local arg_value="$1"
    local arg_name="$2"
    local subcommand_name="$3" # e.g., "greet" or "ping"

    if [ -z "$arg_value" ]; then
        log_error "Missing required argument '${arg_name}' for '${subcommand_name}' command."
        show_help
        exit 1
    fi
}
