#
# def group_lines(features):
#     groups = []
#
#
#     for index, feature in enumerate(features):
#         for ind, feat in enumerate(features):
#             if index == ind:
#                 continue
#
#             if


def associate_input(features, input):
    features = sorted(list(features), reverse=True, key=lambda d: d[0])
    input = sorted(list(input), reverse=True, key=lambda i: i[1]).copy()

    associations = {}
    for index, (x, y) in enumerate(features):
        claimed = []
        associations[index] = []

        for ind, entry in enumerate(input):  # go through words
            (term, x_mid, y_mid) = entry
            if x_mid < x or abs(y - y_mid) > 50:            # check if it should be associated
                continue

            associations[index].append(entry)
            claimed.append(ind)

        # delete once paired
        for ind in reversed(claimed):
            input.pop(ind)

    return associations
