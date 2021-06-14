import matplotlib.pyplot as plt

def draw_hist(df_2006, df_2016, df_2006_T1, df_2016_T1, feature_label, is_percentage=False, bins=20):
    fig, axs = plt.subplots(2,2, figsize=(12,11))
    axs[0][0].hist(df_2006[f'{feature_label}_2006'], bins=bins)
    axs[0][1].hist(df_2016[f'{feature_label}_2016'], bins=bins)
    axs[1][0].hist(df_2006_T1[f'{feature_label}_2006'], bins=bins)
    axs[1][1].hist(df_2016_T1[f'{feature_label}_2016'], bins=bins)

    axs[0][0].set_title('2006')
    axs[0][0].set_ylabel('Occurences')
    axs[0][0].set_xlabel(feature_label + ' (Nice)')
    if is_percentage:
        axs[0][0].set_xlim(xmin=0, xmax=100)
    # axs[0][0].set_ylim(ymin=0, ymax=200)

    axs[0][1].set_title('2016')
    axs[0][1].set_ylabel('Occurences')
    axs[0][1].set_xlabel(feature_label + ' (Nice)')
    if is_percentage:
        axs[0][1].set_xlim(xmin=0, xmax=100)
    # axs[0][1].set_ylim(ymin=0, ymax=200)

    axs[1][0].set_title('2006')
    axs[1][0].set_ylabel('Occurences')
    axs[1][0].set_xlabel(feature_label + ' (T1)')
    if is_percentage:
        axs[1][0].set_xlim(xmin=0, xmax=100)
    # axs[1][0].set_ylim(ymin=0, ymax=9)

    axs[1][1].set_title('2016')
    axs[1][1].set_ylabel('Occurences')
    axs[1][1].set_xlabel(feature_label + ' (T1)')
    if is_percentage:
        axs[1][1].set_xlim(xmin=0, xmax=100)
    # axs[1][1].set_ylim(ymin=0, ymax=9)

    fig.suptitle(feature_label)
    plt.show()
