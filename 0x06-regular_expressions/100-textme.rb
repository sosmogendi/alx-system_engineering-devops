#!/usr/bin/env ruby

def extract_info(log_entry)
  sender = log_entry.match(/\[from:(.*?)\]/)[1]
  receiver = log_entry.match(/\[to:(.*?)\]/)[1]
  flags = log_entry.match(/\[flags:(.*?)\]/)[1]
  "#{sender},#{receiver},#{flags}"
end

# Main script
if __FILE__ == $PROGRAM_NAME
  log_entry = ARGV[0]
  result = extract_info(log_entry)
  puts result
end
