def learn_theta(data, colors):
  max_blue = -float('inf')

  for val, color in zip(data, colors):
    if color == "blue" and val > max_blue:
      max_blue = val

  return max_blue

def compute_ell(data, colors, theta):
  wrong = 0

  for val, color in zip(data, colors):
      if color == "blue" and val > theta:
        wrong += 1
      else if color == "red" and val <= theta:
        wrong += 1

  return float(wrong)

def minimize_ell(data, colors):
  min_loss = float('inf')
  min_theta = 0.0

  for point in data:
    loss = compute_ell(data, colors, point)
    if loss < min_loss:
      min_loss = loss
      min_theta = point

  return min_theta

def minimize_ell_sorted(data, colors):
  total_blue = len(data) / 2

  red_le_theta = 0
  blue_gt_theta = total_blue

  min_loss = red_le_theta + blue_gt_theta
  best_theta = -float('inf')

  for i in range(len(data)):
    color = colors[i]
    point = data[i]

    if color == "blue":
      blue_gt_theta -= 1
    else: 
      red_le_theta += 1

    current_loss = red_le_theta + blue_gt_theta

    if current_loss < min_loss:
      min_loss = current_loss
      best_theta = point
      
  return best_theta
