def generate_bank_standard_projections(base_revenue, base_expenses, scenario='realistic'):
    """
    Generates Cash Flow, Income Statement, and Balance Sheet stubs for a 3-year period.
    Logic includes Conservative, Realistic, and Optimistic scenario multipliers.
    """
    multipliers = {
        'conservative': (1.05, 1.02), # 5% rev growth, 2% exp growth
        'realistic': (1.15, 1.05),    # 15% rev growth, 5% exp growth
        'optimistic': (1.30, 1.10)    # 30% rev growth, 10% exp growth
    }

    rev_mult, exp_mult = multipliers.get(scenario, multipliers['realistic'])

    projections = {
        'income_statement': [],
        'cash_flow': [],
        'balance_sheet_summary': []
    }

    curr_rev = float(base_revenue)
    curr_exp = float(base_expenses)
    curr_cash = 50000.0 # Initial cash assumption
    curr_assets = 200000.0 # Initial assets assumption
    curr_liabilities = 100000.0 # Initial liabilities assumption

    for year in range(1, 4):
        # Income Statement
        net_income = curr_rev - curr_exp
        projections['income_statement'].append({
            'year': year,
            'revenue': round(curr_rev, 2),
            'operating_expenses': round(curr_exp, 2),
            'net_income': round(net_income, 2)
        })

        # Cash Flow (Simplified)
        curr_cash += net_income
        projections['cash_flow'].append({
            'year': year,
            'net_cash_flow': round(net_income, 2),
            'ending_cash_balance': round(curr_cash, 2)
        })

        # Balance Sheet (Simplified)
        curr_equity = curr_assets - curr_liabilities + net_income
        projections['balance_sheet_summary'].append({
            'year': year,
            'total_assets': round(curr_assets, 2),
            'total_liabilities': round(curr_liabilities, 2),
            'total_equity': round(curr_equity, 2)
        })

        # Update for next year
        curr_rev *= rev_mult
        curr_exp *= exp_mult
        curr_assets *= 1.05 # 5% asset appreciation

    return projections

def get_business_plan_template(context='Namibian SME'):
    """
    Returns a guided template structure for a business plan.
    """
    return {
        'sections': [
            {
                'title': 'Executive Summary',
                'guide': 'Summarize your business, unique value proposition, and funding needs.',
                'example': 'Our SME aims to provide affordable solar solutions to rural Namibian communities.'
            },
            {
                'title': 'Market Analysis',
                'guide': 'Describe your target customers and competitors in the Namibian context.',
                'example': 'Targeting farmers in the Erongo region who need off-grid energy.'
            },
            {
                'title': 'Operations & Management',
                'guide': 'Who is on your team and how do you operate day-to-day?',
                'example': 'Managed by a team of 3 with combined 15 years experience in renewable energy.'
            }
        ]
    }
