import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
import locale

locale.setlocale(locale.LC_ALL, "")

def create_chart():
    ### creating the lists and dictionary from the data the user provided
    step = 0
    first_investment = float(initial_investment_entry.get())
    monthly_contribution = float(monthly_contribution_entry.get())
    investment_period = int(investment_period_entry.get())
    estimated_yearly_interest = float(estimated_yearly_interest_entry.get())
    interest_rate_variance_range = float(interest_rate_variance_range_entry.get())

    years_invested = [number for number in range(0, investment_period+1)]

    step_money_amount_list = []
    step_money_amount_list_lower = []
    step_money_amount_list_higher = []
    step_money_amount_list.append(first_investment)
    step_money_amount_list_higher.append(first_investment)
    step_money_amount_list_lower.append(first_investment)

    ### calculating all the yearly steps with interest
    for num in range(0, investment_period):

        formula_flat_interest = ((estimated_yearly_interest/100)*(step_money_amount_list[step] + (12*monthly_contribution)))
        new_money_step = (step_money_amount_list[step] + (12*monthly_contribution)) + formula_flat_interest
        step_money_amount_list.append(new_money_step)

        formula_higher_interest = (((estimated_yearly_interest + interest_rate_variance_range) / 100) * (step_money_amount_list_higher[step] + (12 * monthly_contribution)))
        new_money_step_higher = (step_money_amount_list_higher[step] + (12*monthly_contribution)) + formula_higher_interest
        step_money_amount_list_higher.append(new_money_step_higher)

        formula_lower_interest = (((estimated_yearly_interest - interest_rate_variance_range) / 100) * (step_money_amount_list_lower[step] + (12 * monthly_contribution)))
        new_money_step_lower = (step_money_amount_list_lower[step] + (12*monthly_contribution)) + formula_lower_interest
        step_money_amount_list_lower.append(new_money_step_lower)

        step += 1

    ###creating the dataframe from our data in the dictionary
    dataframe_dictionary = {"years": years_invested, "money earned estimation":step_money_amount_list, "lower range interest rate":step_money_amount_list_lower ,"higher range interest rate":step_money_amount_list_higher}
    df = pd.DataFrame(data=dataframe_dictionary)
    sns.set_style("whitegrid")
    plt.figure(figsize=(11, 5))
    sns.lineplot(data=df, linewidth=2, markers=True, palette="rocket").set(title="money earned (estimate)",
                                                         xlabel="years", ylabel="money earned")
    #specifications for notations on the chart
    plt.annotate((f"{int(step_money_amount_list[-1]):n}$\n in {investment_period} years\n at {estimated_yearly_interest}% interest"), xy=(investment_period - 0.5, step_money_amount_list[-2]), ha="center", bbox=dict(boxstyle="square,pad=0.3", fc="#B270A2", ec="#411530"))
    plt.annotate((f"{int(step_money_amount_list_lower[-1]):n}$\n in {investment_period} years\n at {(estimated_yearly_interest - interest_rate_variance_range)}% interest"), xy=(investment_period -0.5, step_money_amount_list_lower[-4]), ha="center", bbox=dict(boxstyle="square,pad=0.3", fc="#DF7861", ec="#411530"))
    plt.annotate((f"{int(step_money_amount_list_higher[-1]):n}$\n in {investment_period} years\n at {(estimated_yearly_interest + interest_rate_variance_range)}% interest"), xy=(investment_period -0.5, step_money_amount_list_higher[-1]), ha="center", bbox=dict(boxstyle="square,pad=0.3", fc="#FFDEB4" ,ec="#411530"))
    plt.legend(bbox_to_anchor=(0.1, 0.95), loc=2)
    plt.show()

### Tkinter Gui build
window = Tk()
window.title("Compound Interest Calculator")
window.geometry("900x800")

space_label = Label(text="")
space_label.grid(column=1, row=0)

initial_investment_label = Label(text="initial investment:", font=("david", 20), padx=10)
initial_investment_label.grid(column=1, row=1, sticky="w", padx=50, pady=6)

initial_investment_entry = Entry(width=50)
initial_investment_entry.insert(END, string="0")
initial_investment_entry.grid(column=2, row=1)

monthly_contribution_label = Label(text="monthly contribution:", font=("david", 20), padx=10)
monthly_contribution_label.grid(column=1, row=2, sticky="w", padx=50, pady=6)

monthly_contribution_entry = Entry(width=50)
monthly_contribution_entry.insert(END, string="0")
monthly_contribution_entry.grid(column=2, row=2)


investment_period_label = Label(text="investment period in years:", font=("david", 20), padx=10)
investment_period_label.grid(column=1, row=3, sticky="w", padx=50, pady=6)

investment_period_entry = Entry(width=50)
investment_period_entry.insert(END, string="0")
investment_period_entry.grid(column=2, row=3)


estimated_yearly_interest_label = Label(text="estimated yearly interest in %:", font=("david", 20), padx=10)
estimated_yearly_interest_label.grid(column=1, row=4, sticky="w", padx=50, pady=6)

estimated_yearly_interest_entry = Entry(width=50)
estimated_yearly_interest_entry.insert(END, string="0")
estimated_yearly_interest_entry.grid(column=2, row=4)


interest_rate_variance_range_label = Label(text="interest rate possible change in %:", font=("david", 20), padx=10)
interest_rate_variance_range_label.grid(column=1, row=5, sticky="w", padx=50, pady=6)

interest_rate_variance_range_entry = Entry(width=50)
interest_rate_variance_range_entry.insert(END, string="0")
interest_rate_variance_range_entry.grid(column=2, row=5)

go_button = PhotoImage(file="letts go.png")
calculate_button = Button(image=go_button, bd=0, command=create_chart)
calculate_button.grid(column=1, row=6, columnspan=2, sticky="s", padx=30, pady=30)

canvas = Canvas(width=700, height=300, highlightthickness=0)
money_image = PhotoImage(file="money_image.PNG")
canvas_image = canvas.create_image(350, 90, image=money_image)
canvas.grid(column=1, row=7, columnspan=2, padx=100, sticky="s")


window.mainloop()



