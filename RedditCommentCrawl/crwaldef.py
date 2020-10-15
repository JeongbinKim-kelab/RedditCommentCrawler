
def parse_submission(submission):
    return {
        'title': submission.title,
        #'post_key' : post_key,
        #'created_utc': submission.created_utc,
        'author_fullname': submission.author_fullname,
        #'selftext': submission.selftext,
        #'selftext_html': submission.selftext_html,
        'id': submission.id,
        'num_comments' : submission.num_comments,
        'create_utc': submission.created_utc
    }


def parse_comment(comment):
    return {
        'body': comment.body,
        'parent_id': comment.parent_id,
        'id': comment.id,
        'create_utc': comment.created_utc,
        'permalink': comment.permalink,
        #'replies': comment.replies,
        'depth': comment.depth,
        'parent': comment.parent()
    }

def print_Data(data):
    for key, value in data.items():
        print(key, " : ", value)
    print('\n')
    return
    
    
def comment_Preprocessing(comments):
    temp = []
    for comment in comments:
        if comment['depth'] != 0 and comment['parent_id'][:3] != 't3_':
            temp.append(comment)
    return temp


def all_Find_Depth(comment, all_list):
    depth = 1
    copy_leaf = comment
    check = comment['body']
    temp = comment['parent']
    while temp.parent_id[:3] != 't3_':
        depth += 1
        temp = temp.parent()
    depth += 1
    copy_root = temp
    #print(temp.body, " ", depth)
    all_list.append([copy_root, copy_leaf, depth])
    

def tree_Clean(all_List):
    temp = []
    result = []
    for i in all_List:
        if len(temp) != 3 and i[0] not in temp:
            temp.append(i[0])
            result.append(i)
    return result


def in_top3(tree):
    temp = []
    temp1 = []
    check = tree['body']
    temp.append(check)
    temp1.append(tree['id'])
    print(tree['id'])
    check = tree['parent']
    while check.parent_id[:3] != 't3_':
        temp.append(check.body)
        temp1.append(check.id)
        print(check.id)
        check = check.parent()
    temp.append(check.body)
    temp1.append(check.id)
    print(check.id)
    check = check.parent()
    temp.append(check.title)
    temp1.append(check.id)
    return temp, temp1

def jump_Comment(comments):
    temp = []
    for line in comments:
        for i in range(len(line)-1, 0, -1):
            temp.append([line[i], line[i-1]])
    return temp