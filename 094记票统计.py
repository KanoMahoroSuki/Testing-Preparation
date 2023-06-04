candidate_count = int(input())
candidates = input().split(' ')
voter_count = int(input())
votes = input().split(' ')

votes_dict = {candidate: 0 for candidate in candidates}
votes_dict['Invalid'] = 0

for vote in votes:
    if vote in votes_dict:
        votes_dict[vote] += 1
    else:
        votes_dict['Invalid'] += 1

for candidate, vote_count in votes_dict.items():
    print(f"{candidate} : {vote_count}")
