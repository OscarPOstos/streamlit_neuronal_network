def neuronal_net(weight, input):
  return weight * input

def neuronal_net_2(weight_1, weight_2, input_1, input_2):
  return weight_1 * input_1 + weight_2 * input_2

def neuronal_net_3(weight_1, weight_2, weight_3, bias, input_1, input_2, input_3):
  return weight_1 * input_1 + weight_2 * input_2 + weight_3 * input_3 + bias