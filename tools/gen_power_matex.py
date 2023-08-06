import os
from os import path

def periodic_power_logs(directory_path):

     with open(os.path.join(directory_path, 'PeriodicPower.log'), 'r') as f:

          first_line_flag = False
          output_values = []
          time_count = -1
          for line in f:
               final_values = []
               temp_values = []
               values = line.split('\t')
               if not first_line_flag:
                    final_values.append('time')
                    [final_values.append(values[idx]) for idx in range(len(values) - 1)]
                    first_line_flag = True
               else:
                    final_values.append(time_count)
                    [final_values.append(float(values[idx])) for idx in range(len(values) - 1)]
                    time_count = time_count + 1
               [temp_values.append(str(val)) for val in final_values]
               output_values.append(temp_values)
     f.close()
     with open(os.path.join(directory_path, 'MatexPower.log'), 'w') as f:
          for items in output_values:
               f.write('\t'.join(items) + '\n')
     f.close()
