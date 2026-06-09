"""
NyayaAI — Indian Legal Clause Database
Curated clauses for RAG-based document generation
"""

CLAUSE_DATABASE = {
    "nda": [
        {
            "id": "nda_001",
            "title": "Definition of Confidential Information",
            "text": "\"Confidential Information\" means any data or information, oral or written, relating to the business, technical, financial, operational activities, trade secrets, know-how, customer lists, pricing information, or any other proprietary information of the Disclosing Party that is designated as confidential or that reasonably should be understood to be confidential given the nature of the information and circumstances of disclosure.",
            "act": "Indian Contract Act, 1872 - Section 27",
            "category": "confidentiality",
            "risk_level": "low"
        },
        {
            "id": "nda_002",
            "title": "Obligations of Receiving Party",
            "text": "The Receiving Party agrees to: (a) hold the Confidential Information in strict confidence; (b) not disclose the Confidential Information to any third party without prior written consent; (c) use the Confidential Information solely for the Purpose; (d) protect the Confidential Information using the same degree of care as it uses for its own confidential information, but no less than reasonable care; (e) restrict access to Confidential Information to those of its employees, contractors, or agents who need to know such information.",
            "act": "Indian Contract Act, 1872",
            "category": "confidentiality",
            "risk_level": "medium"
        },
        {
            "id": "nda_003",
            "title": "Exclusions from Confidentiality",
            "text": "The obligations of confidentiality shall not apply to information that: (a) is or becomes publicly known through no breach of this Agreement; (b) was rightfully known to the Receiving Party without restriction before disclosure; (c) is independently developed by the Receiving Party without use of Confidential Information; (d) is rightfully received from a third party without restriction; (e) is required to be disclosed by law, court order, or governmental authority, provided the Receiving Party gives prompt written notice to the Disclosing Party.",
            "act": "Indian Contract Act, 1872",
            "category": "confidentiality",
            "risk_level": "low"
        },
        {
            "id": "nda_004",
            "title": "Term and Duration",
            "text": "This Agreement shall be effective from the date of signing and shall continue for the agreed duration. The confidentiality obligations shall survive termination of this Agreement for a period of two (2) years thereafter, or until the Confidential Information enters the public domain through no fault of the Receiving Party.",
            "act": "Indian Contract Act, 1872",
            "category": "term",
            "risk_level": "medium"
        },
        {
            "id": "nda_005",
            "title": "Return or Destruction of Information",
            "text": "Upon termination of this Agreement or upon the Disclosing Party's written request, the Receiving Party shall promptly return or certifiably destroy all Confidential Information, including all copies, extracts, and derivatives thereof, and shall provide written certification of such destruction within five (5) business days.",
            "act": "Indian Contract Act, 1872",
            "category": "confidentiality",
            "risk_level": "low"
        },
        {
            "id": "nda_006",
            "title": "Injunctive Relief",
            "text": "The parties acknowledge that any breach of this Agreement may cause irreparable harm for which monetary damages would be an inadequate remedy. Accordingly, the non-breaching party shall be entitled to seek injunctive relief and specific performance in any court of competent jurisdiction, without the necessity of proving actual damages or posting a bond or other security.",
            "act": "Specific Relief Act, 1963",
            "category": "remedies",
            "risk_level": "high"
        },
        {
            "id": "nda_007",
            "title": "Non-Compete Clause",
            "text": "During the term of this Agreement and for a period of one (1) year following its termination, the Receiving Party shall not, directly or indirectly, engage in any business activity that directly competes with the Disclosing Party within the territory of India, without prior written consent. Note: Post-employment non-compete may have limited enforceability under Indian law.",
            "act": "Indian Contract Act, 1872 - Section 27",
            "category": "non_compete",
            "risk_level": "high"
        },
        {
            "id": "nda_008",
            "title": "Non-Solicitation Clause",
            "text": "During the term of this Agreement and for a period of two (2) years following its termination, the Receiving Party shall not solicit, recruit, or hire any employees, contractors, or customers of the Disclosing Party who were introduced to the Receiving Party through this Agreement.",
            "act": "Indian Contract Act, 1872",
            "category": "non_solicitation",
            "risk_level": "medium"
        }
    ],
    "rental": [
        {
            "id": "rental_001",
            "title": "Grant of License to Use Premises",
            "text": "The Licensor hereby grants to the Licensee a revocable, non-transferable license to use and occupy the residential premises described herein, on a leave and license basis only. This Agreement shall not create any tenancy, sub-tenancy, or any other interest in the said premises in favour of the Licensee.",
            "act": "Transfer of Property Act, 1882 - Section 105",
            "category": "grant",
            "risk_level": "low"
        },
        {
            "id": "rental_002",
            "title": "License Fee and Payment Terms",
            "text": "The Licensee shall pay the License Fee on or before the 5th day of each calendar month. In case of delay beyond 10 days, the Licensor shall be entitled to charge interest at the rate of 2% per month on the outstanding amount. All payments shall be made by NEFT/RTGS/UPI to the bank account designated by the Licensor.",
            "act": "Transfer of Property Act, 1882",
            "category": "payment",
            "risk_level": "medium"
        },
        {
            "id": "rental_003",
            "title": "Security Deposit",
            "text": "The Licensee shall deposit an amount as Security Deposit, which shall be refundable without interest at the time of vacation of the premises, subject to deduction of: (a) any unpaid License Fee or dues; (b) cost of damages to the premises beyond normal wear and tear; (c) any unpaid utility charges. The Security Deposit shall be returned within 30 days of vacation of the premises and completion of all formalities.",
            "act": "Transfer of Property Act, 1882",
            "category": "security",
            "risk_level": "high"
        },
        {
            "id": "rental_004",
            "title": "Lock-In Period",
            "text": "This Agreement shall have a lock-in period from the commencement date. During the lock-in period, neither party shall be entitled to terminate this Agreement. In the event of premature vacation by the Licensee during the lock-in period, the Licensee shall forfeit the Security Deposit. In the event of premature revocation by the Licensor, the Licensor shall pay to the Licensee an amount equivalent to two months' License Fee as compensation.",
            "act": "Transfer of Property Act, 1882",
            "category": "lock_in",
            "risk_level": "medium"
        },
        {
            "id": "rental_005",
            "title": "Maintenance and Repairs",
            "text": "The Licensee shall maintain the premises in clean and habitable condition. Minor repairs up to INR 1,000/- per incident shall be carried out by the Licensee at their expense. Major structural repairs and plumbing work shall be carried out by the Licensor. The Licensee shall not make any structural alterations to the premises without prior written consent of the Licensor.",
            "act": "Transfer of Property Act, 1882",
            "category": "maintenance",
            "risk_level": "low"
        },
        {
            "id": "rental_006",
            "title": "Utilities and Charges",
            "text": "The Licensee shall be responsible for payment of all electricity, water, gas, internet, and other utility charges consumed during the license period. The Licensor shall not be held responsible for any interruption in utility services. Society maintenance charges shall be borne by the Licensor unless otherwise agreed.",
            "act": "Transfer of Property Act, 1882",
            "category": "utilities",
            "risk_level": "low"
        },
        {
            "id": "rental_007",
            "title": "Notice Period and Termination",
            "text": "Either party may terminate this Agreement by giving written notice of the agreed notice period. Upon expiry of the notice period, the Licensee shall peacefully vacate the premises and hand over all keys, access cards, and other items belonging to the premises. The Licensor shall carry out an inspection and issue a no-objection certificate within 7 days thereafter.",
            "act": "Transfer of Property Act, 1882",
            "category": "termination",
            "risk_level": "medium"
        }
    ],
    "employment": [
        {
            "id": "emp_001",
            "title": "Appointment and Designation",
            "text": "The Employee is hereby appointed to the position of [Designation] in the [Department] department, reporting to [Reporting Manager]. The Employee's primary place of work shall be [Location], subject to change as per business requirements. The Employer reserves the right to transfer the Employee to any other location, department, or subsidiary.",
            "act": "Industrial Disputes Act, 1947",
            "category": "appointment",
            "risk_level": "low"
        },
        {
            "id": "emp_002",
            "title": "Compensation and Benefits",
            "text": "The Employee shall receive a Cost to Company (CTC) as specified in the offer letter, inclusive of basic salary, house rent allowance, special allowances, and applicable statutory contributions including Provident Fund and ESI. The salary shall be credited to the Employee's designated bank account on or before the last working day of each month.",
            "act": "Payment of Wages Act, 1936; Employees' Provident Funds Act, 1952",
            "category": "compensation",
            "risk_level": "low"
        },
        {
            "id": "emp_003",
            "title": "Probation Period",
            "text": "The Employee shall be on probation for the period specified from the Date of Joining. During the probation period, either party may terminate the employment by giving 7 days' written notice or payment in lieu thereof. Upon successful completion of probation, the appointment shall be confirmed in writing.",
            "act": "Industrial Disputes Act, 1947",
            "category": "probation",
            "risk_level": "medium"
        },
        {
            "id": "emp_004",
            "title": "Intellectual Property Assignment",
            "text": "All inventions, discoveries, developments, improvements, computer programs, designs, works of authorship, and other work product created by the Employee, whether alone or jointly with others, in the course of employment or using the Employer's resources, shall be the sole and exclusive property of the Employer. The Employee agrees to execute all documents necessary to perfect the Employer's ownership rights.",
            "act": "Patents Act, 1970; Copyright Act, 1957",
            "category": "ip_assignment",
            "risk_level": "high"
        },
        {
            "id": "emp_005",
            "title": "Confidentiality and Non-Disclosure",
            "text": "The Employee shall maintain strict confidentiality of all proprietary, technical, commercial, financial, and business information of the Employer during the term of employment and for a period of two (2) years after termination, regardless of the reason for termination. Breach of this clause shall entitle the Employer to seek injunctive relief and claim damages.",
            "act": "Indian Contract Act, 1872",
            "category": "confidentiality",
            "risk_level": "high"
        },
        {
            "id": "emp_006",
            "title": "Termination and Notice Period",
            "text": "Either party may terminate this Agreement by providing written notice of the agreed notice period, or by payment of salary in lieu of notice. The Employer may terminate the employment immediately for cause, including gross misconduct, fraud, dishonesty, or willful breach of any term of this Agreement, without notice or payment in lieu thereof.",
            "act": "Industrial Disputes Act, 1947; Shops and Establishments Act",
            "category": "termination",
            "risk_level": "medium"
        },
        {
            "id": "emp_007",
            "title": "Non-Compete (Post-Employment)",
            "text": "For a period of twelve (12) months following cessation of employment, the Employee shall not directly or indirectly engage with competing businesses in the same domain. Note: Courts in India have generally held post-employment non-compete clauses unenforceable under Section 27 of the Indian Contract Act, 1872. This clause is included for good-faith compliance.",
            "act": "Indian Contract Act, 1872 - Section 27",
            "category": "non_compete",
            "risk_level": "high"
        },
        {
            "id": "emp_008",
            "title": "Moonlighting Policy",
            "text": "The Employee shall devote their full time, attention, and skills exclusively to the business of the Employer during working hours. The Employee shall not engage in any other employment, consultancy, or business activity without prior written approval from the Employer. Violation of this clause shall be grounds for immediate termination.",
            "act": "Industrial Disputes Act, 1947",
            "category": "moonlighting",
            "risk_level": "medium"
        }
    ],
    "freelance": [
        {
            "id": "fl_001",
            "title": "Scope of Work and Deliverables",
            "text": "The Service Provider agrees to provide the services as described in Schedule A ('Scope of Work') attached hereto. Any work beyond the agreed scope shall require a written Change Order signed by both parties before commencement. The Service Provider shall not subcontract any part of the work without prior written consent of the Client.",
            "act": "Indian Contract Act, 1872",
            "category": "scope",
            "risk_level": "high"
        },
        {
            "id": "fl_002",
            "title": "Fees and Payment Schedule",
            "text": "The Client shall pay the Service Provider as per the agreed payment schedule. All invoices are payable within 15 business days of receipt. Late payments beyond 30 days shall attract interest at 2% per month. All fees are exclusive of applicable GST, which shall be charged additionally at prevailing rates.",
            "act": "Indian Contract Act, 1872; CGST Act, 2017",
            "category": "payment",
            "risk_level": "medium"
        },
        {
            "id": "fl_003",
            "title": "Intellectual Property Ownership",
            "text": "Upon receipt of full and final payment, all deliverables, including but not limited to designs, code, content, reports, and any work product created under this Agreement, shall become the sole and exclusive property of the Client. Until full payment is received, all IP rights remain with the Service Provider, and the Client shall have no right to use any deliverables.",
            "act": "Copyright Act, 1957; Patents Act, 1970",
            "category": "ip",
            "risk_level": "high"
        },
        {
            "id": "fl_004",
            "title": "Independent Contractor Status",
            "text": "The Service Provider is an independent contractor and not an employee, partner, or agent of the Client. The Service Provider is solely responsible for payment of all applicable taxes, including income tax and GST. The Client shall not be responsible for providing any employee benefits, and this Agreement does not create any employer-employee relationship.",
            "act": "Income Tax Act, 1961; CGST Act, 2017",
            "category": "contractor_status",
            "risk_level": "medium"
        },
        {
            "id": "fl_005",
            "title": "Kill Fee / Cancellation",
            "text": "In the event the Client cancels the project after commencement, the Client shall pay a kill fee as follows: (a) 25% of the project fee if cancelled before 25% completion; (b) 50% if cancelled between 25-50% completion; (c) 75% if cancelled after 50% completion; (d) 100% if cancelled after 75% completion. Work completed to the cancellation date remains the Client's property.",
            "act": "Indian Contract Act, 1872",
            "category": "cancellation",
            "risk_level": "medium"
        }
    ],
    "partnership": [
        {
            "id": "part_001",
            "title": "Constitution of Partnership",
            "text": "The Partners hereby agree to carry on business in partnership under the firm name and style as specified, subject to the provisions of the Indian Partnership Act, 1932 / Limited Liability Partnership Act, 2008. The partnership shall be governed by the terms and conditions set forth in this Deed and in accordance with applicable law.",
            "act": "Indian Partnership Act, 1932; LLP Act, 2008",
            "category": "constitution",
            "risk_level": "low"
        },
        {
            "id": "part_002",
            "title": "Capital Contribution",
            "text": "Each partner shall contribute capital to the partnership as specified in Schedule A. Additional capital may be introduced by mutual written consent. No partner shall withdraw capital without the unanimous consent of all partners. Capital accounts shall be maintained separately and interest on capital shall be credited at the agreed rate.",
            "act": "Indian Partnership Act, 1932",
            "category": "capital",
            "risk_level": "medium"
        },
        {
            "id": "part_003",
            "title": "Profit and Loss Sharing",
            "text": "The net profits and losses of the partnership business shall be shared among the partners in the ratios specified herein. The accounts of the partnership shall be maintained on accrual basis and shall be audited annually by a Chartered Accountant. Final accounts shall be drawn up as of March 31 each year.",
            "act": "Indian Partnership Act, 1932; Income Tax Act, 1961",
            "category": "profit_sharing",
            "risk_level": "medium"
        },
        {
            "id": "part_004",
            "title": "Management and Voting",
            "text": "All partners shall participate in the management of the business. Ordinary business decisions shall be made by simple majority. Decisions regarding admission of new partners, capital expenditure beyond INR 10,00,000, change in business nature, dissolution, or winding up shall require unanimous consent of all partners.",
            "act": "Indian Partnership Act, 1932",
            "category": "management",
            "risk_level": "medium"
        }
    ],
    "legalnotice": [
        {
            "id": "ln_001",
            "title": "Notice to Cure Breach",
            "text": "TAKE NOTICE that my client has instructed me to inform you that you have committed a breach of the Agreement dated [Date] by failing to [specify breach]. You are hereby called upon to remedy the said breach within [X] days from the receipt of this notice, failing which my client shall be constrained to initiate appropriate legal proceedings before the competent court, without any further notice, and at your risk as to costs and consequences.",
            "act": "Indian Contract Act, 1872 - Section 73, 74",
            "category": "breach",
            "risk_level": "high"
        },
        {
            "id": "ln_002",
            "title": "Recovery of Money",
            "text": "TAKE NOTICE that a sum of INR [Amount] (Rupees [Amount in words] only) is due and payable by you to my client as on date in respect of [specify nature of dues]. You are called upon to pay the said amount within [X] days from the date of receipt of this notice, failing which my client shall be constrained to file appropriate legal proceedings for recovery of the said amount along with interest, costs, and damages.",
            "act": "Indian Contract Act, 1872; Code of Civil Procedure, 1908",
            "category": "recovery",
            "risk_level": "high"
        }
    ],
    "general": [
        {
            "id": "gen_001",
            "title": "Governing Law and Jurisdiction",
            "text": "This Agreement shall be governed by and construed in accordance with the laws of India. Any dispute arising out of or in connection with this Agreement shall be subject to the exclusive jurisdiction of the courts located in [City], India.",
            "act": "Civil Procedure Code, 1908",
            "category": "governing_law",
            "risk_level": "low"
        },
        {
            "id": "gen_002",
            "title": "Arbitration Clause",
            "text": "Any dispute, controversy, or claim arising out of or relating to this Agreement, including the breach, termination, or invalidity thereof, shall be finally settled by arbitration in accordance with the Arbitration and Conciliation Act, 1996. The arbitration shall be conducted by a sole arbitrator mutually appointed by the parties. The seat of arbitration shall be [City], India, and the proceedings shall be conducted in English.",
            "act": "Arbitration and Conciliation Act, 1996",
            "category": "dispute_resolution",
            "risk_level": "medium"
        },
        {
            "id": "gen_003",
            "title": "Force Majeure",
            "text": "Neither party shall be liable for any failure or delay in performance of its obligations under this Agreement to the extent such failure or delay is caused by circumstances beyond its reasonable control, including but not limited to acts of God, floods, earthquakes, epidemics, pandemics, government actions, war, civil unrest, or failure of telecommunications infrastructure. The affected party shall notify the other party promptly and use reasonable efforts to resume performance.",
            "act": "Indian Contract Act, 1872 - Section 56",
            "category": "force_majeure",
            "risk_level": "low"
        },
        {
            "id": "gen_004",
            "title": "Entire Agreement",
            "text": "This Agreement constitutes the entire agreement between the parties with respect to the subject matter hereof and supersedes all prior negotiations, representations, warranties, and understandings of the parties. No modification, amendment, or waiver of any provision of this Agreement shall be effective unless made in writing and signed by both parties.",
            "act": "Indian Contract Act, 1872",
            "category": "entire_agreement",
            "risk_level": "low"
        },
        {
            "id": "gen_005",
            "title": "Severability",
            "text": "If any provision of this Agreement is held to be invalid, illegal, or unenforceable by a court of competent jurisdiction, such provision shall be modified to the minimum extent necessary to make it valid and enforceable, and the remaining provisions of this Agreement shall continue in full force and effect.",
            "act": "Indian Contract Act, 1872",
            "category": "severability",
            "risk_level": "low"
        },
        {
            "id": "gen_006",
            "title": "Notices",
            "text": "All notices, demands, or communications under this Agreement shall be in writing and delivered by: (a) registered post with acknowledgment due; (b) courier with proof of delivery; (c) email with read receipt; to the addresses specified herein. Notices shall be deemed received upon delivery or, if sent by email, upon transmission.",
            "act": "Indian Contract Act, 1872; IT Act, 2000",
            "category": "notices",
            "risk_level": "low"
        },
        {
            "id": "gen_007",
            "title": "Indemnification",
            "text": "Each party (\"Indemnifying Party\") shall defend, indemnify, and hold harmless the other party and its officers, directors, employees, and agents from and against any and all claims, damages, losses, costs, and expenses (including reasonable attorneys' fees) arising out of or resulting from the Indemnifying Party's: (a) breach of this Agreement; (b) negligence or willful misconduct; (c) infringement of third-party intellectual property rights.",
            "act": "Indian Contract Act, 1872 - Section 124-125",
            "category": "indemnification",
            "risk_level": "high"
        },
        {
            "id": "gen_008",
            "title": "Limitation of Liability",
            "text": "In no event shall either party be liable to the other for any indirect, incidental, consequential, special, exemplary, or punitive damages, regardless of the theory of liability and even if such party has been advised of the possibility of such damages. Each party's total liability under this Agreement shall not exceed the total fees paid or payable under this Agreement in the twelve months preceding the claim.",
            "act": "Indian Contract Act, 1872",
            "category": "liability",
            "risk_level": "high"
        }
    ]
}

# Flat list of all clauses for FAISS indexing
ALL_CLAUSES = []
for doc_type, clauses in CLAUSE_DATABASE.items():
    for clause in clauses:
        clause["doc_type"] = doc_type
        ALL_CLAUSES.append(clause)

# Indian Legal Acts Reference
INDIAN_ACTS = {
    "Indian Contract Act, 1872": "Governs all contracts and agreements in India. Covers offer, acceptance, consideration, breach, and remedies.",
    "Transfer of Property Act, 1882": "Governs transfer of immovable property including sale, mortgage, lease, and gift.",
    "Indian Partnership Act, 1932": "Governs partnership firms in India, including formation, rights, and dissolution.",
    "LLP Act, 2008": "Governs Limited Liability Partnerships in India.",
    "Companies Act, 2013": "Governs companies, directors, corporate governance, and mergers.",
    "Industrial Disputes Act, 1947": "Governs employment disputes, layoffs, and labour rights.",
    "Payment of Wages Act, 1936": "Governs timely payment of wages to employees.",
    "Employees' Provident Funds Act, 1952": "Mandatory PF contributions for employees.",
    "IT Act, 2000": "Governs electronic contracts, digital signatures, cybercrime, and data privacy.",
    "Copyright Act, 1957": "Protects literary, artistic, and software works.",
    "Patents Act, 1970": "Governs patent protection in India.",
    "Arbitration and Conciliation Act, 1996": "Governs arbitration proceedings in India.",
    "Consumer Protection Act, 2019": "Protects consumer rights and regulates unfair trade practices.",
    "CGST Act, 2017": "Central Goods and Services Tax for B2B and B2C transactions.",
    "Specific Relief Act, 1963": "Provides for specific performance of contracts and injunctive relief.",
}
