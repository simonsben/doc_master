def associate_input(features, data_input):
    features = sorted(list(features), reverse=True, key=lambda d: d[0])
    data_input = sorted(list(data_input), reverse=True, key=lambda i: i[1]).copy()

    associations = {}
    for index, (x, y) in enumerate(features):
        claimed = []
        associations[index] = []

        for ind, entry in enumerate(data_input):  # go through words
            (term, x_mid, y_mid) = entry
            if x_mid < x or abs(y - y_mid) > 50:            # check if it should be associated
                continue

            associations[index].append(entry)
            claimed.append(ind)

        # delete once paired
        for ind in reversed(claimed):
            data_input.pop(ind)

    return [list(features[ind]) + associations[ind] for ind in associations]


def clean_associations(associations):
    content = []
    for association in associations:
        information = ''
        for word in reversed(association[2:]):
            information += word[0] + ' '

        content.append(information)

    return content

