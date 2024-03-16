import app.io.input as inp
import app.io.output as out


def main():
    con_inp = inp.console_input()
    out.console_output(con_inp)
    out.file_output_default(con_inp, './data/con_out.txt')

    print('=' * 40)

    file_inp = inp.read_file_default('./data/def_test.txt')
    out.console_output(file_inp)
    out.file_output_default(file_inp, './data/def_out.txt')

    print('=' * 40)

    file_inp_pd = inp.read_csv_file_pd('./data/pd_test.csv')
    out.console_output(file_inp_pd)
    out.file_output_default(file_inp_pd, './data/def_pd_out.txt')


if __name__ == '__main__':
    main()
