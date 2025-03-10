import streamlit as st
import random

def reset_game():
    st.session_state['number'] = random.randint(st.session_state['min_range'], st.session_state['max_range'])
    st.session_state['attempts'] = 0
    st.session_state['message'] = ""
    st.session_state['game_over'] = False

def main():
    st.title("🎯 Number Guessing Game")
    
    if 'min_range' not in st.session_state:
        st.session_state['min_range'] = 1
    if 'max_range' not in st.session_state:
        st.session_state['max_range'] = 100
    if 'difficulty' not in st.session_state:
        st.session_state['difficulty'] = 'Unlimited'
    
    st.sidebar.header("Game Settings")
    min_val = st.sidebar.number_input("Minimum Number", min_value=1, value=1, step=1)
    max_val = st.sidebar.number_input("Maximum Number", min_value=min_val + 1, value=100, step=1)
    difficulty = st.sidebar.selectbox("Difficulty", ['Unlimited', 'Easy (10 attempts)', 'Medium (7 attempts)', 'Hard (5 attempts)'])
    
    if st.sidebar.button("Start New Game") or 'number' not in st.session_state:
        st.session_state['min_range'] = min_val
        st.session_state['max_range'] = max_val
        st.session_state['difficulty'] = difficulty
        reset_game()
    
    max_attempts = {'Unlimited': float('inf'), 'Easy (10 attempts)': 10, 'Medium (7 attempts)': 7, 'Hard (5 attempts)': 5}
    allowed_attempts = max_attempts[st.session_state['difficulty']]
    
    st.write(f"Guess a number between {st.session_state['min_range']} and {st.session_state['max_range']}")
    
    guess = st.number_input("Enter your guess", min_value=st.session_state['min_range'], max_value=st.session_state['max_range'], step=1, key='guess_input')
    
    if st.button("Submit Guess") and not st.session_state['game_over']:
        st.session_state['attempts'] += 1
        
        if guess < st.session_state['number']:
            st.session_state['message'] = "🔼 Too low! Try again."
        elif guess > st.session_state['number']:
            st.session_state['message'] = "🔽 Too high! Try again."
        else:
            st.session_state['message'] = f"🎉 Congratulations! You guessed the number in {st.session_state['attempts']} attempts."
            st.session_state['game_over'] = True
        
        if st.session_state['attempts'] >= allowed_attempts:
            st.session_state['message'] = f"😢 Game over! The number was {st.session_state['number']}."
            st.session_state['game_over'] = True
    
    st.write(st.session_state['message'])
    st.write(f"Attempts: {st.session_state['attempts']} / {allowed_attempts if allowed_attempts != float('inf') else '∞'}")
    
    if st.session_state['game_over']:
        if st.button("Play Again"):
            reset_game()

if __name__ == "__main__":
    main()
