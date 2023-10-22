// 获取元素
const messageInput = document.getElementById('message-input');
const submitBtn = document.getElementById('submit-btn');
const chatDisplay = document.querySelector('.chat-display');

// 添加事件监听器
submitBtn.addEventListener('click', sendMessage);

// 定义函数：发送消息
function sendMessage() {
    var space = "&nbsp;&nbsp;";
    // 获取输入的消息内容
    const message = messageInput.value + space;
    
    // 创建一个新的消息元素
    const newMessage = document.createElement('div');
    newMessage.classList.add('message');
    
    // 设置消息内容和样式
    newMessage.innerHTML = message;
    newMessage.style.backgroundColor = '#428bca';
    newMessage.style.color = 'white';
    newMessage.style.padding = '5px 10px';
    newMessage.style.marginBottom = '10px';
    newMessage.style.borderRadius = '10px';
    
    // 将消息添加到对话展示框中
    chatDisplay.appendChild(newMessage);
    
    // 清空输入框
    messageInput.value = '';

    // 获取用户头像的URL
    const avatarUrl = 'https://profile-avatar.csdnimg.cn/0f6aa505e6cc4a888fd612fbf8e4f2e3_qq_21891743.jpg';

    // 创建并设置头像元素
    const avatar = document.createElement('img');
    avatar.src = avatarUrl;
    avatar.width = 40;
    avatar.height = 40;

    // 将头像元素添加到消息元素的前面
    newMessage.appendChild(avatar, newMessage.firstChild);

    // 获取当前用户的用户名
    const username = 'User';

    // 设置消息的样式
    if (username === 'User') {
        // 用户的消息样式
        newMessage.style.backgroundColor = '#428bca';
        newMessage.style.color = 'white';
        newMessage.style['text-align'] = 'right';
        newMessage.style['display'] = 'inline-flex';
        newMessage.style['justify-content'] = 'right'
        newMessage.style['align-items'] = 'center'
        newMessage.style['width'] = '100%'
        sendReplyMessage()
    } else {
        // 对方的消息样式
        newMessage.style.backgroundColor = '#f5f5f5';
        newMessage.style.color = '#333';
    }
}

function sendReplyMessage() {
    // 获取输入的消息内容
    var space = "&nbsp;&nbsp;";
    const message = space + '你的消息我们已经收到，会尽快回复您';
    
    // 创建一个新的消息元素
    const newMessage = document.createElement('div');
    newMessage.classList.add('message');
    
    // 设置消息内容和样式
    newMessage.innerHTML = message;
    newMessage.style.backgroundColor = '#428bca';
    newMessage.style.color = 'white';
    newMessage.style.padding = '5px 10px';
    newMessage.style.marginBottom = '10px';
    
    // 将消息添加到对话展示框中
    chatDisplay.appendChild(newMessage);
    
    // 清空输入框
    messageInput.value = '';

    // 获取用户头像的URL
    const avatarUrl = 'https://g.csdnimg.cn/static/logo/favicon32.ico';

    // 创建并设置头像元素
    const avatar = document.createElement('img');
    avatar.src = avatarUrl;
    avatar.width = 40;
    avatar.height = 40;

    // 将头像元素添加到消息元素的前面
    newMessage.insertBefore(avatar, newMessage.firstChild);

    // 获取当前用户的用户名
    const username = 'Admin';

    // 对方的消息样式
    newMessage.style.backgroundColor = '#f5f5f5';
    newMessage.style.color = '#333';
    newMessage.style['text-align'] = 'right';
    newMessage.style['display'] = 'inline-flex';
    newMessage.style['justify-content'] = 'left'
    newMessage.style['align-items'] = 'center'
    newMessage.style['width'] = '100%'
}


