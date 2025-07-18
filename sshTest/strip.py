test_string = "   Hello DevOps!   \n"
# Make whitespace visible
visible_string = test_string.replace(" ", "·").replace("\n", "¶")
print(f"Before strip: '{visible_string}'")

stripped = test_string.strip()
visible_stripped = stripped.replace(" ", "·").replace("\n", "¶")
print(f"After strip:  '{visible_stripped}'")