def main():

    train_data = np.array(
    [
        [0,0],
        [0,1],
        [1,0],
        [1,1]
    ]
    )

    target_xor = np.array(
        [
            [0],
            [1],
            [1],
            [0]
        ]
    )

    target_nand = np.array(
        [
            [1],
            [1],
            [1],
            [0]
        ]
    )

    target_or = np.array(
        [
            [0],
            [1],
            [1],
            [1]
        ]
    )

    target_and = np.array(
        [
            [0],
            [1],
            [1],
            [1]
        ]
    )

if __name__ == "__main__":
    main()
    