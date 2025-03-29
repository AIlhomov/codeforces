s = list(input())
hello = []

done_h = False
done_e = False
done_l1 = False
done_l2 = False
done_o = False

for c in s:
    if c == "h" and not done_h:
        hello.append("h")
        done_h = True
    if c == "e" and not done_e and done_h:
        hello.append("e")
        done_e = True
    if c == "l" and not done_l1 and done_h and done_e:
        hello.append("l")
        done_l1 = True
        continue #so we dont do the second "l"
    if c == "l" and not done_l2 and done_h and done_e and done_l1:
        hello.append("l")
        done_l2 = True
    if c == "o" and not done_o and done_h and done_e and done_l1 and done_l2:
        hello.append("o")
        done_o = True
if "".join(hello) == "hello":
    print("YES")
else:
    print("NO")
# print(filtered_hello)
# if "h" in filtered_hello and "e" in filtered_hello and "l" in filtered_hello and \
#     "o" in filtered_hello:
#     print("YES")
# else:
#     print("NO")
# i j k m n o p
# done = False
# for i in range(len(s)):
#     if s[i] == "h":
#         for j in range(i, len(s)):
#             if s[j] == "e":
#                 for k in range(j, len(s)):
#                     if s[k] == "l":
#                         for m in range(k, len(s)):
#                             if s[m] == "l":
#                                 for n in range(m, len(s)):
#                                     if done:
#                                         break
#                                     if s[n] == "o":
#                                         print("YES")
#                                         done = True
#                             elif s[m] == "l":
#                                 continue
#                             else:
#                                 break
#                     elif s[k] == "e":
#                         continue
#                     else:
#                         break
#             elif s[j] == "h":
#                 continue
#             else:
#                 break
# if not done:
#     print("NO")