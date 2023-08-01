#!/usr/bin/env ruby

def match_school(input_string)
  # Use the regular expression /School/ to match "School" in the input string
  matched = input_string.scan(/School/)
  matched.join
end

# Main script
if __FILE__ == $PROGRAM_NAME
  input_string = ARGV[0]
  result = match_school(input_string)
  puts result
end
