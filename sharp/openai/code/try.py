import gym
env = gym.make('Copy-v0')
i = 0
while i < 10000:
    i = i + 1
    env.reset()
    env.render()
