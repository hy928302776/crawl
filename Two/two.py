from One.one import test


def two():
    test()

if __name__ == '__main__':
    two()
    st="<em>宁德时代</em>申请注册,<em>宁德时代</em>申请注册"
    print(st.replace('</em>', '').replace('<em>', ''))