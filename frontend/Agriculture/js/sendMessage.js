async function sendMessage() {
    const sendButton = document.getElementById('send-button');
    const chatBox = document.getElementById('chat-box');
    const imageInput = document.getElementById('upload');
    const textInput = document.getElementById('text-input');
    const textContent = textInput.value.trim();

    // 禁用发送按钮
    sendButton.disabled = true;

    // 显示用户消息
    if (textContent) {
        displayMessage(textContent, 'user-message');
    }
    // 清除输入框
    textInput.value = '';
    imageInput.value = '';
    // 将图像转换为 Base64
    let imageBase64 = '';
    if (imageInput.files.length > 0) {
        imageBase64 = await toBase64(imageInput.files[0]);
    }

    // 创建请求数据
    const payload = {
        model: "internvl2-1b",
        messages: [{
            role: "user",
            content: [{
                    type: "image_url",
                    image_url: {
                        url: imageBase64 ? imageBase64 : ""
                    }
                },
                {
                    type: "text",
                    text: textContent
                }
            ]
        }],
        temperature: 0
    };

    try {
        const response = await fetch('http://192.168.135.79:8000/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer EMPTY',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        });

        const data = await response.json();

        // 检查响应是否包含消息
        if (data.choices && data.choices.length > 0) {
            const assistantMessage = data.choices[0].message.content;
            displayMessage(assistantMessage, 'response-message');
        } else {
            displayMessage('No response from the assistant.', 'response-message');
        }
    } catch (error) {
        console.error('Error:', error);
        displayMessage('Error occurred, please try again.', 'response-message');
    } finally {
        // 响应处理完成后，启用发送按钮
        sendButton.disabled = false;
    }
    //测试语句
    // displayMessage('No response from the assistant.', 'response-message');
    // sendButton.disabled = false;
}


// 将文件转换为 Base64
function toBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });
}

// 在聊天框中显示消息
function displayMessage(message, className) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${className}`;
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}