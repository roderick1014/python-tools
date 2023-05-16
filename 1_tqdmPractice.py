from tqdm import tqdm
import time

def progressBar(epochs, iterations, pause_delay):
    start_time = time.time()

    for epoch in range(1, epochs):

        progress_bar = tqdm(range(iterations))

        for idx in progress_bar:
            time.sleep(pause_delay)
            progress_bar.set_description_str(f'Epoch: {epoch}')
            progress_bar.set_postfix(val = idx)

        time_consume = time.time() - start_time
        print(f'Epoch {epoch} Finished. It took {time_consume} seconds.')

    print('Training finished.')
    print('Consuming Time: ', time.time() - start_time)


if __name__ == '__main__':

    epochs = 5
    iterations = 100
    pause_delay = 0.005
    progressBar(epochs, iterations, pause_delay)