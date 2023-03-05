from time import sleep

'''
1520-2791,2842, 3351-3836,4214-4225,4812,4814,4816,4899-5013, 5039, 5047-5085, 5099,5137-5139,5172-5251,5300, 5310,5399-5411, 5441, 5511-5542, 5691, 5811-5812, 5814,5941-5942,5964, 5969-5970,5992, 7011, 7296,7332-7349,7393-7511,7524-7534, 7549,7692-7699, 7829-7832,7929, 7933-7941, 7991, 7996, 8011, 8398-8641, 8699-8734, 8999,9222,9399,

0742-3090,3094-5085, 5099-5310, 5331-5661, 5691-5722,5733-5815,5817-5932,5935 -5943,5946-5999,6050-7261, 7276,7278-7296, 7298-7321,7332-7699, 7829-7994, 7996- 8641,8675-9222,9311-9399,9402-9752,9950,

0742-3090,3094-5085, 5099-5310,5331-5661,5691-5722,5733-5815,5817-5932,5935 - 5943,5946-5999, 6050-7261,7276,7278-7296, 7298-7321,7332-7699,7829-7994,7996- 8641,8675-9222,9311-9399,9402-9752,9950,
'''

MCC_LIST = [742, 763, 780, 1520, 1711, 1731, 1740, 1750, 1761, 1771, 1799, 2732, 2741, 2791, 2842, 3000, 3001, 3002, 3003, 3004, 3005, 3006, 3007, 3008, 3009, 3010, 3011, 3012, 3013, 3014, 3015, 3016, 3017, 3018, 3019, 3020, 3021, 3022, 3023, 3024, 3025, 3026, 3027, 3028, 3029, 3030, 3031, 3032, 3033, 3034, 3035, 3036, 3037, 3038, 3039, 3040, 3041, 3042, 3043, 3044, 3045, 3046, 3047, 3048, 3049, 3050, 3051, 3052, 3053, 3054, 3055, 3056, 3057, 3058, 3059, 3060, 3061, 3062, 3063, 3064, 3065, 3066, 3067, 3068, 3069, 3070, 3071, 3072, 3073, 3075, 3076, 3077, 3078, 3079, 3081, 3082, 3083, 3084, 3085, 3086, 3087, 3088, 3089, 3090, 3094, 3096, 3097, 3098, 3099, 3100, 3102, 3103, 3105, 3106, 3110, 3111, 3112, 3115, 3117, 3118, 3125, 3126, 3127, 3129, 3130, 3131, 3132, 3133, 3135, 3136, 3137, 3138, 3141, 3143, 3144, 3145, 3146, 3148, 3151, 3154, 3156, 3159, 3161, 3164, 3165, 3167, 3170, 3171, 3172, 3174, 3175, 3176, 3177, 3178, 3180, 3181, 3182, 3183, 3184, 3185, 3186, 3187, 3188, 3190, 3191, 3192, 3193, 3195, 3196, 3197, 3198, 3199, 3200, 3203, 3204, 3206, 3207, 3211, 3212, 3213, 3215, 3216, 3217, 3218, 3219, 3220, 3221, 3222, 3223, 3226, 3228, 3229, 3231, 3233, 3234, 3235, 3236, 3238, 3239, 3240, 3241, 3242, 3243, 3245, 3246, 3247, 3248, 3251, 3252, 3253, 3254, 3256, 3259, 3260, 3261, 3262, 3263, 3266, 3267, 3268, 3275, 3276, 3277, 3279, 3280, 3282, 3284, 3285, 3286, 3287, 3291, 3292, 3293, 3294, 3295, 3296, 3297, 3298, 3299, 3300, 3301, 3303, 3308, 3351, 3352, 3353, 3354, 3355, 3357, 3359, 3360, 3361, 3362, 3364, 3366, 3368, 3370, 3374, 3376, 3380, 3381, 3385, 3386, 3387, 3388, 3389, 3390, 3391, 3393, 3394, 3395, 3396, 3398, 3400, 3405, 3409, 3412, 3414, 3420, 3421, 3423, 3425, 3427, 3428, 3429, 3430, 3431, 3432, 3433, 3434, 3435, 3436, 3437, 3438, 3439, 3441, 3501, 3502, 3503, 3504, 3505, 3506, 3507, 3508, 3509, 3510, 3511, 3512, 3513, 3514, 3515, 3516, 3517, 3518, 3519, 3520, 3521, 3522, 3523, 3524, 3525, 3526, 3527, 3528, 3529, 3530, 3531, 3532, 3533, 3534, 3535, 3536, 3537, 3538, 3539, 3540, 3541, 3542, 3543, 3544, 3545, 3546, 3547, 3548, 3549, 3550, 3551, 3552, 3553, 3554, 3555, 3556, 3557, 3558, 3559, 3560, 3561, 3562, 3563, 3564, 3565, 3566, 3567, 3568, 3569, 3570, 3571, 3572, 3573, 3574, 3575, 3576, 3577, 3578, 3579, 3580, 3581, 3582, 3583, 3584, 3585, 3586, 3587, 3588, 3589, 3590, 3591, 3592, 3593, 3594, 3595, 3596, 3597, 3598, 3599, 3600, 3601, 3602, 3603, 3604, 3605, 3606, 3607, 3608, 3609, 3610, 3611, 3612, 3613, 3614, 3615, 3616, 3617, 3618, 3619, 3620, 3621, 3622, 3623, 3624, 3625, 3626, 3627, 3628, 3629, 3630, 3631, 3632, 3633, 3634, 3635, 3636, 3637, 3638, 3639, 3640, 3641, 3642, 3643, 3644, 3645, 3646, 3647, 3648, 3649, 3650, 3651, 3652, 3653, 3654, 3655, 3656, 3657, 3658, 3659, 3660, 3661, 3662, 3663, 3664, 3665, 3666, 3667, 3668, 3669, 3670, 3671, 3672, 3673, 3674, 3675, 3676, 3677, 3678, 3679, 3680, 3681, 3682, 3683, 3684, 3685, 3686, 3687, 3688, 3689, 3690, 3691, 3692, 3693, 3694, 3695, 3696, 3697, 3698, 3699, 3700, 3701, 3702, 3703, 3704, 3705, 3706, 3707, 3708, 3709, 3710, 3711, 3712, 3713, 3714, 3715, 3716, 3717, 3718, 3719, 3720, 3721, 3722, 3723, 3724, 3725, 3726, 3727, 3728, 3729, 3730, 3731, 3732, 3733, 3734, 3735, 3736, 3737, 3738, 3739, 3740, 3741, 3742, 3743, 3744, 3745, 3746, 3747, 3748, 3749, 3750, 3751, 3752, 3753, 3754, 3755, 3756, 3757, 3758, 3759, 3760, 3761, 3762, 3763, 3764, 3765, 3766, 3767, 3768, 3769, 3770, 3771, 3772, 3773, 3774, 3775, 3776, 3777, 3778, 3779, 3780, 3781, 3782, 3783, 3784, 3785, 3786, 3787, 3788, 3789, 3790, 3791, 3792, 3793, 3794, 3795, 3796, 3797, 3798, 3799, 3800, 3801, 3802, 3803, 3804, 3805, 3806, 3807, 3808, 3809, 3810, 3811, 3812, 3813, 3814, 3815, 3816, 3817, 3818, 3819, 3820, 3821, 3822, 3823, 3824, 3825, 3826, 3827, 3828, 3829, 3830, 3831, 3832, 3833, 3834, 3835, 3836, 3837, 3838, 3998, 4011, 4111, 4112, 4119, 4121, 4131, 4214, 4215, 4225, 4411, 4457, 4468, 4511, 4582, 4722, 4723, 4761, 4784, 4785, 4789, 4812, 4813, 4814, 4815, 4816, 4821, 4829, 4899, 4900, 5013, 5021, 5039, 5044, 5045, 5046, 5047, 5051, 5065, 5072, 5074, 5085, 5094, 5099, 5111, 5122, 5131, 5137, 5139, 5169, 5172, 5192, 5193, 5198, 5199, 5200, 5211, 5231, 5251, 5261, 5262, 5271, 5300, 5309, 5310, 5311, 5331, 5399, 5411, 5422, 5441, 5451, 5462, 5499, 5511, 5521, 5531, 5532, 5533, 5541, 5542, 5551, 5552, 5561, 5571, 5592, 5598, 5599, 5611, 5621, 5631, 5641, 5651, 5655, 5661, 5681, 5691, 5697, 5698, 5699, 5712, 5713, 5714, 5715, 5718, 5719, 5722, 5732, 5733, 5734, 5735, 5811, 5812, 5813, 5814, 5815, 5816, 5817, 5818, 5912, 5921, 5931, 5932, 5933, 5935, 5937, 5940, 5941, 5942, 5943, 5944, 5945, 5946, 5947, 5948, 5949, 5950, 5960, 5961, 5962, 5963, 5964, 5965, 5966, 5967, 5968, 5969, 5970, 5971, 5972, 5973, 5975, 5976, 5977, 5978, 5983, 5992, 5993, 5994, 5995, 5996, 5997, 5998, 5999, 6010, 6011, 6012, 6050, 6051, 6051, 6211, 6300, 6381, 6399, 6513, 6529, 6530, 6531, 6532, 6533, 6534, 6535, 6536, 6537, 6538, 6540, 6555, 7011, 7012, 7013, 7032, 7033, 7210, 7211, 7216, 7217, 7221, 7230, 7251, 7261, 7273, 7276, 7277, 7278, 7296, 7297, 7298, 7299, 7311, 7321, 7322, 7332, 7333, 7338, 7339, 7342, 7349, 7361, 7372, 7375, 7379, 7392, 7393, 7394, 7395, 7399, 7511, 7512, 7513, 7519, 7523, 7524, 7531, 7534, 7535, 7538, 7539, 7542, 7549, 7622, 7623, 7629, 7631, 7641, 7692, 7699, 7778, 7800, 7801, 7802, 7829, 7832, 7841, 7911, 7922, 7929, 7932, 7933, 7941, 7990, 7991, 7992, 7993, 7994, 7995, 7996, 7997, 7998, 7999, 8011, 8021, 8031, 8041, 8042, 8043, 8044, 8049, 8050, 8062, 8071, 8099, 8111, 8211, 8220, 8241, 8244, 8249, 8299, 8351, 8398, 8641, 8651, 8661, 8675, 8699, 8734, 8911, 8931, 8999, 9211, 9222, 9223, 9311, 9399, 9401, 9402, 9405, 9406, 9700, 9701, 9702, 9751, 9752, 9753, 9754, 9950]

template_mcc = input('**Copy and paste template list from TSYS:\n>> ')

template_mcc_list = template_mcc.split(',')

active_list = []

for mcc in template_mcc_list:
    if len(mcc) <= 2:
        pass
    elif '-' in mcc:
        sub_template_mcc_list = mcc.split('-')
        low_limit = int(sub_template_mcc_list[0])
        high_limit = int(sub_template_mcc_list[1]) + 1
        for mcc_code in range(low_limit, high_limit):
            if mcc_code in MCC_LIST:
                active_list.append(mcc_code)
    else:
        mcc_code = int(mcc)
        active_list.append(mcc_code)

template_type = input('**Template type: Enter I for include or E for Exclude\n>> ').lower()
write_file = input('**Do you want to save the output to a file?: y or n\n>> ').lower()
if write_file == 'y':
    file_name = input('**Enter file name and extension. txt, csv, xls:\n>> ')
    file = open(f'test-code\\{file_name}', 'w')
    file.write('MCC  Status\n')
else:
    print('Result will not be saved to file')
    sleep(2)

print('MCC  Status')
for code in MCC_LIST:
    code = code if len(str(code)) == 4 else f'0{code}'
    if template_type == 'i':        
        if write_file == 'y':
            file.write(f'{code} unblocked\n' if code in active_list else f'{code} blocked\n')
        print(f'{code} unblocked' if code in active_list else f'{code} blocked')
    elif template_type == 'e':        
        if write_file == 'y':
            file.write(f'{code} blocked\n' if code in active_list else f'{code} unblocked\n')
        print(f'{code} blocked' if code in active_list else f'{code} unblocked')
    else:
        print('Template type error!!!  Start again.')
        break

if write_file == 'y':
    file.close()
    print(f'The output has been saved in "{file_name}"!!!')
