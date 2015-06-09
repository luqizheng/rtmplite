import rtmp,multitask

agent = rtmp.FlashServer()
agent.root = './'
agent.start('0.0.0.0', 1935)

multitask.run()
